# Copyright 2024 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Annotated, Any, List

import datetime
import re

from pydantic import AfterValidator, BeforeValidator, PlainSerializer

# Initialize our RE statically, rather than compiling for every call. This has
# the downside that it'll get compiled at import time but that shouldn't
# really be a big deal.
reDuration = re.compile(r'^([0-9]{1,5}(h|m|s|ms)){1,4}$')

# maxDuration_ms is the maximum duration that GEP-2257 can support, in
# milliseconds.
maxDuration_ms = (((99999 * 3600) + (59 * 60) + 59) * 1_000) + 999

# Go's time.Duration format and range.
reGoDuration = re.compile(r'[-+]?(0|(([0-9]+\.?[0-9]*|\.[0-9]+)(ns|us|\u00b5s|\u03bcs|ms|s|m|h))+)')
maxGoDuration = datetime.timedelta(microseconds=(2 ** 63 - 1) // 1000)

_DURATION_UNIT_NS = {
    'ns': 1,
    'us': 1_000,
    '\u00b5s': 1_000,
    '\u03bcs': 1_000,
    'ms': 1_000_000,
    's': 1_000_000_000,
    'm': 60 * 1_000_000_000,
    'h': 3600 * 1_000_000_000,
}
_RE_DURATION_PART = re.compile(r'([0-9]+\.?[0-9]*|\.[0-9]+)(ns|us|\u00b5s|\u03bcs|ms|s|m|h)')


def _duration_from_str(duration: str) -> datetime.timedelta:
    """Parse a Go-style duration string into a datetime.timedelta."""
    if duration in ("0", "+0", "-0"):
        return datetime.timedelta(0)

    sign = -1 if duration.startswith("-") else 1
    s = duration.lstrip("+-")

    total_ns = 0.0
    try:
        for match in _RE_DURATION_PART.finditer(s):
            val_str, unit = match.groups()
            total_ns += float(val_str) * _DURATION_UNIT_NS[unit]

        microseconds = round(sign * total_ns / 1_000)
        return datetime.timedelta(microseconds=microseconds)
    except (OverflowError, ValueError) as e:
        raise ValueError("Duration out of range: {}".format(duration)) from e


def parse_duration(duration: str) -> datetime.timedelta:
    """
    Parse GEP-2257 Duration format to a datetime.timedelta object.

    The GEP-2257 Duration format is a restricted form of the input to the Go
    time.ParseDuration function; specifically, it must match the regex
    "^([0-9]{1,5}(h|m|s|ms)){1,4}$".

    See https://gateway-api.sigs.k8s.io/geps/gep-2257/ for more details.

    Input: duration: string
    Returns: datetime.timedelta

    Raises: ValueError on invalid or unknown input

    Examples:
    >>> parse_duration("1h")
    datetime.timedelta(seconds=3600)
    >>> parse_duration("1m")
    datetime.timedelta(seconds=60)
    >>> parse_duration("1s")
    datetime.timedelta(seconds=1)
    >>> parse_duration("1ms")
    datetime.timedelta(microseconds=1000)
    >>> parse_duration("1h1m1s")
    datetime.timedelta(seconds=3661)
    >>> parse_duration("10s30m1h")
    datetime.timedelta(seconds=5410)

    Units are always required.
    >>> parse_duration("1")
    Traceback (most recent call last):
        ...
    ValueError: Invalid duration format: 1

    Floating-point and negative durations are not valid.
    >>> parse_duration("1.5m")
    Traceback (most recent call last):
        ...
    ValueError: Invalid duration format: 1.5m
    >>> parse_duration("-1m")
    Traceback (most recent call last):
        ...
    ValueError: Invalid duration format: -1m
    """

    if not reDuration.match(duration):
        raise ValueError("Invalid duration format: {}".format(duration))

    return _duration_from_str(duration)


def format_duration(delta: datetime.timedelta) -> str:
    """
    Format a datetime.timedelta object to GEP-2257 Duration format.

    The GEP-2257 Duration format is a restricted form of the input to the Go
    time.ParseDuration function; specifically, it must match the regex
    "^([0-9]{1,5}(h|m|s|ms)){1,4}$".

    See https://gateway-api.sigs.k8s.io/geps/gep-2257/ for more details.

    Input: duration: datetime.timedelta

    Returns: string

    Raises: ValueError if the timedelta given cannot be expressed as a
    GEP-2257 Duration.

    Examples:
    >>> format_duration(datetime.timedelta(seconds=3600))
    '1h'
    >>> format_duration(datetime.timedelta(seconds=60))
    '1m'
    >>> format_duration(datetime.timedelta(seconds=1))
    '1s'
    >>> format_duration(datetime.timedelta(microseconds=1000))
    '1ms'
    >>> format_duration(datetime.timedelta(seconds=5410))
    '1h30m10s'

    The zero duration is always "0s".
    >>> format_duration(datetime.timedelta(0))
    '0s'

    Sub-millisecond precision is not allowed.
    >>> format_duration(datetime.timedelta(microseconds=100))
    Traceback (most recent call last):
        ...
    ValueError: Cannot express sub-millisecond precision in GEP-2257: 0:00:00.000100

    Negative durations are not allowed.
    >>> format_duration(datetime.timedelta(seconds=-1))
    Traceback (most recent call last):
        ...
    ValueError: Cannot express negative durations in GEP-2257: -1 day, 23:59:59
    """

    # Short-circuit if we have a zero delta.
    if delta == datetime.timedelta(0):
        return "0s"

    # Check range early.
    if delta < datetime.timedelta(0):
        raise ValueError("Cannot express negative durations in GEP-2257: {}".format(delta))

    if delta > datetime.timedelta(milliseconds=maxDuration_ms):
        raise ValueError(
            "Cannot express durations longer than 99999h59m59s999ms in GEP-2257: {}".format(delta))

    # GEP-2257 does not allow floating-point seconds. So start by peeling off any microseconds
    # from our delta.
    delta_us = delta.microseconds

    if (delta_us % 1000) != 0:
        raise ValueError(
            "Cannot express sub-millisecond precision in GEP-2257: {}"
            .format(delta)
        )

    # After that, do the usual div & mod tree to take seconds and get hours,
    # minutes, and seconds from it.
    secs = int(delta.total_seconds())

    output: List[str] = []

    hours = secs // 3600
    if hours > 0:
        output.append(f"{hours}h")
        secs -= hours * 3600

    minutes = secs // 60
    if minutes > 0:
        output.append(f"{minutes}m")
        secs -= minutes * 60

    if secs > 0:
        output.append(f"{secs}s")

    if delta_us > 0:
        output.append(f"{delta_us // 1000}ms")

    return "".join(output)


def _parse_go_duration(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    if not reGoDuration.fullmatch(value):
        raise ValueError("Invalid duration format: {}".format(value))
    return _duration_from_str(value)


def _check_go_duration_range(value: datetime.timedelta) -> datetime.timedelta:
    if abs(value) > maxGoDuration:
        raise ValueError("Duration out of range: {}".format(value))
    return value


def _decimal(value: int, digits: int) -> str:
    whole, frac = divmod(value, 10 ** digits)
    if not frac:
        return str(whole)
    return "{}.{}".format(whole, str(frac).zfill(digits).rstrip("0"))


def _format_go_duration(value: datetime.timedelta) -> str:
    sign = "-" if value < datetime.timedelta(0) else ""
    us = abs(value) // datetime.timedelta(microseconds=1)
    if us == 0:
        return "0s"
    if us < 1000:
        return "{}{}us".format(sign, us)
    if us < 1_000_000:
        return "{}{}ms".format(sign, _decimal(us, 3))

    hours, us = divmod(us, 3_600_000_000)
    minutes, us = divmod(us, 60_000_000)
    seconds = _decimal(us, 6)
    if hours:
        return "{}{}h{}m{}s".format(sign, hours, minutes, seconds)
    if minutes:
        return "{}{}m{}s".format(sign, minutes, seconds)
    return "{}{}s".format(sign, seconds)


# metav1.Duration for pydantic models
Duration = Annotated[
    datetime.timedelta,
    BeforeValidator(_parse_go_duration),
    AfterValidator(_check_go_duration_range),
    PlainSerializer(_format_go_duration, return_type=str),
]
