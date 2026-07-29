# Copyright 2026 The Kubernetes Authors.
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

import re
from dataclasses import dataclass
from typing import Any, Callable, Optional


# This module contains common pieces for 1:1 Python implementations of the
# Kubernetes Go retry algorithms used by client-go:
# - https://github.com/kubernetes/client-go/blob/master/util/retry/util.go
# - https://github.com/kubernetes/apimachinery/blob/master/pkg/util/wait/
#   backoff.go
# - https://github.com/kubernetes/client-go/blob/master/rest/with_retry.go
# Backoff durations are represented as seconds instead of time.Duration.
@dataclass(frozen=True)
class Backoff:
    """Retry backoff parameters.

    This maps 1:1 to ``k8s.io/apimachinery/pkg/util/wait.Backoff`` for the
    fields used by client-go retry helpers. ``steps`` is the maximum number of
    times the operation is called, including the first call. ``duration`` is
    the first delay in seconds, ``factor`` is multiplied into the next delay
    after every failed attempt, and ``jitter`` adds up to that fraction of the
    current delay. ``cap`` limits increased delay values.
    """

    steps: int
    duration: float
    factor: float
    jitter: float = 0.0
    cap: float = 0.0

    def __post_init__(self):
        if self.steps < 1:
            raise ValueError("steps must be at least 1")
        if self.duration < 0:
            raise ValueError("duration must be non-negative")
        if self.factor < 0:
            raise ValueError("factor must be non-negative")
        if self.jitter < 0:
            raise ValueError("jitter must be non-negative")
        if self.cap < 0:
            raise ValueError("cap must be non-negative")


# 1:1 with k8s.io/client-go/util/retry.DefaultBackoff.
DEFAULT_BACKOFF = Backoff(steps=4, duration=0.01, factor=5.0, jitter=0.1)

# 1:1 with k8s.io/client-go/util/retry.DefaultRetry.
DEFAULT_RETRY = Backoff(steps=5, duration=0.01, factor=1.0, jitter=0.1)

# Matches rest.Request's default response retry ceiling: one initial attempt
# plus 10 retries after Retry-After responses.
DEFAULT_RETRY_AFTER_BACKOFF = Backoff(
    steps=11, duration=0.0, factor=1.0, jitter=0.0)


def retry_after_backoff(
    retries: Any = None,
    backoff: Optional[Backoff] = None,
) -> Backoff:
    """Return the client-go REST Retry-After backoff for ``retries``.

    ``backoff`` supplies the retry delay parameters. If ``retries`` is not
    ``None``, it is interpreted as the retry ceiling and overrides
    ``backoff.steps``. ``False`` and ``0`` disable retries by returning a
    single-attempt backoff. Integer values and urllib3-style Retry objects with
    a ``total`` value are treated as the retry ceiling.
    """

    if backoff is None:
        backoff = DEFAULT_RETRY_AFTER_BACKOFF
    if retries is None:
        return backoff

    return Backoff(
        steps=retry_after_max_retries(retries) + 1,
        duration=backoff.duration,
        factor=backoff.factor,
        jitter=backoff.jitter,
        cap=backoff.cap,
    )


def retry_after_max_retries(retries: Any = None) -> int:
    """Return the client-go REST Retry-After retry ceiling."""

    if retries is None:
        return 10
    if retries is False:
        return 0
    if retries is True:
        return 10
    if isinstance(retries, int):
        return max(0, retries)

    total = getattr(retries, "total", None)
    if total is False:
        return 0
    if total is True or total is None:
        return 10
    if isinstance(total, int):
        return max(0, total)
    return 10


def is_conflict(error: Exception) -> bool:
    """Return True if ``error`` represents an HTTP 409 Conflict response."""

    return getattr(error, "status", None) == 409


def is_too_many_requests(error: Exception) -> bool:
    """Return True if ``error`` represents HTTP 429 Too Many Requests."""

    return getattr(error, "status", None) == 429


def is_retry_after_response(error: Exception) -> bool:
    """Return True if ``error`` should be retried after Retry-After."""

    status = getattr(error, "status", None)
    if status != 429 and (status is None or status < 500):
        return False
    return retry_after_seconds(error) is not None


def retry_after_seconds(error: Exception) -> Optional[float]:
    """Return the Retry-After delay in seconds, if ``error`` provides one.

    client-go accepts integer seconds. Invalid, missing, or negative values
    return ``None`` so callers can fall back to their normal backoff.
    """

    headers = getattr(error, "headers", None) or {}
    value = None
    for key, header_value in headers.items():
        if key.lower() == "retry-after":
            value = header_value
            break
    if value is None:
        return None

    value = str(value).strip()
    if not re.match(r"^[0-9]+$", value):
        return None
    return float(int(value))


def _delay(
    steps: int,
    duration: float,
    backoff: Backoff,
    random_func: Callable[[], float],
) -> tuple[float, float, int]:
    steps -= 1
    if backoff.factor == 0:
        next_duration = duration
    else:
        next_duration = duration * backoff.factor
        if backoff.cap > 0 and next_duration > backoff.cap:
            next_duration = backoff.cap
            steps = 0
    delay = duration
    if backoff.jitter:
        delay += random_func() * backoff.jitter * delay
    return delay, next_duration, steps
