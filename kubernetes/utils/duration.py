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
import datetime
import re

import durationpy

# Initialize our RE statically, rather than compiling for every call. This has
# the downside that it'll get compiled at import time but that shouldn't
# really be a big deal.
reDuration = re.compile(r'^([0-9]{1,5}(h|m|s|ms)){1,4}$')

# maxDuration_ms is the maximum duration that GEP-2257 can support, in milliseconds.
maxDuration_ms = (((99999 * 3600) + (59 * 60) + 59) * 1_000) + 999

def parse_duration(duration) -> datetime.timedelta:
    """
    Parse GEP-2257 Duration format to a datetime.timedelta object.

    The GEP-2257 Duration format is a restricted form of the input to the Go
    time.ParseDuration function; specifically, it must match the regex
    "^([0-9]{1,5}(h|m|s|ms)){1,4}$".

    See https://gateway-api.sigs.k8s.io/geps/gep-2257/ for more details.

    Input: duration: string

    Returns: datetime.timedelta

    Raises: ValueError on invalid or unknown input
    """

    if not reDuration.match(duration):
        raise ValueError("Invalid duration format: {}".format(duration))

    return durationpy.from_str(duration)

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
    """

    # Short-circuit if we have a zero delta.
    if delta == datetime.timedelta(0):
        return "0s"

    # Check range early.
    if delta < datetime.timedelta(0):
        raise ValueError("Cannot express negative durations in GEP-2257: {}".format(delta))

    if delta > datetime.timedelta(milliseconds=maxDuration_ms):
        raise ValueError("Cannot express durations longer than 99999h59m59s999ms in GEP-2257: {}".format(delta))

    # durationpy.to_str() is happy to use floating-point seconds, which
    # GEP-2257 is _not_ happy with. So start by peeling off any microseconds
    # from our delta.
    delta_us = delta.microseconds

    if (delta_us % 1000) != 0:
        raise ValueError(
            "Cannot express sub-millisecond precision in GEP-2257: {}"
            .format(delta)
        )

    # Second short-circuit.

    delta -= datetime.timedelta(microseconds=delta_us)
    delta_ms = delta_us // 1000
    delta_str = durationpy.to_str(delta)

    if delta_ms > 0:
        # We have milliseconds to add back in. Make sure to not have a leading
        # "0" if we have no other duration components.
        if delta == datetime.timedelta(0):
            delta_str = ""

        delta_str += f"{delta_ms}ms"

    return delta_str

