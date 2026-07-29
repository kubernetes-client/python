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

import random
import time
from typing import Callable, TypeVar

from ._retry_base import (
    Backoff,
    DEFAULT_BACKOFF,
    DEFAULT_RETRY,
    DEFAULT_RETRY_AFTER_BACKOFF,
    _delay,
    is_conflict,
    is_retry_after_response,
    is_too_many_requests,
    retry_after_backoff,
    retry_after_max_retries,
    retry_after_seconds,
)


T = TypeVar("T")


# The retry helpers in this module are 1:1 Python implementations of the
# Kubernetes Go retry algorithms used by client-go:
# - https://github.com/kubernetes/client-go/blob/master/util/retry/util.go
# - https://github.com/kubernetes/client-go/blob/master/rest/with_retry.go
def on_error(
    backoff: Backoff,
    retriable: Callable[[Exception], bool],
    fn: Callable[[], T],
    sleep_func: Callable[[float], None] = time.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Run ``fn`` and retry while ``retriable`` returns True.

    This is a 1:1 implementation of
    ``k8s.io/client-go/util/retry.OnError``.
    """

    steps = backoff.steps
    duration = backoff.duration
    last_error = None
    while steps > 0:
        try:
            return fn()
        except Exception as error:
            if not retriable(error):
                raise
            last_error = error

            if steps == 1:
                break

            delay, duration, steps = _delay(
                steps, duration, backoff, random_func)
            sleep_func(delay)

    raise last_error


def retry_on_conflict(
    fn: Callable[[], T],
    backoff: Backoff = DEFAULT_RETRY,
    sleep_func: Callable[[float], None] = time.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Run ``fn`` and retry on HTTP 409 Conflict responses.

    This is a 1:1 implementation of
    ``k8s.io/client-go/util/retry.RetryOnConflict``. Callers should re-read the
    object inside ``fn`` before each write attempt, so every retry uses the
    latest resource version.
    """

    return on_error(backoff, is_conflict, fn, sleep_func, random_func)


def on_retry_after_error(
    backoff: Backoff,
    retriable: Callable[[Exception], bool],
    fn: Callable[[], T],
    sleep_func: Callable[[float], None] = time.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Run ``fn`` with client-go REST Retry-After sleep semantics.

    This is a 1:1 implementation of the wait selection in
    ``k8s.io/client-go/rest.WithRetry``: if the retriable response carries a
    valid ``Retry-After`` header, that delay is used; otherwise the supplied
    backoff delay is used.
    """

    steps = backoff.steps
    duration = backoff.duration
    last_error = None
    while steps > 0:
        try:
            return fn()
        except Exception as error:
            if not retriable(error):
                raise
            last_error = error

            if steps == 1:
                break

            delay, duration, steps = _delay(
                steps, duration, backoff, random_func)
            retry_after = retry_after_seconds(error)
            if retry_after is not None and retry_after > delay:
                delay = retry_after
            sleep_func(delay)

    raise last_error
