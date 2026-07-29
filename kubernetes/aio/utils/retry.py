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

import asyncio
import random
from typing import Awaitable, Callable, TypeVar

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


# The retry helpers in this module are async 1:1 Python implementations of the
# Kubernetes Go retry algorithms used by client-go:
# - https://github.com/kubernetes/client-go/blob/master/util/retry/util.go
# - https://github.com/kubernetes/client-go/blob/master/rest/with_retry.go
async def on_error(
    backoff: Backoff,
    retriable: Callable[[Exception], bool],
    fn: Callable[[], Awaitable[T]],
    sleep_func: Callable[[float], Awaitable[None]] = asyncio.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Async 1:1 implementation of client-go ``retry.OnError``."""

    steps = backoff.steps
    duration = backoff.duration
    last_error = None
    while steps > 0:
        try:
            return await fn()
        except Exception as error:
            if not retriable(error):
                raise
            last_error = error

            if steps == 1:
                break

            delay, duration, steps = _delay(
                steps, duration, backoff, random_func)
            await sleep_func(delay)

    raise last_error


async def retry_on_conflict(
    fn: Callable[[], Awaitable[T]],
    backoff: Backoff = DEFAULT_RETRY,
    sleep_func: Callable[[float], Awaitable[None]] = asyncio.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Async 1:1 implementation of client-go ``retry.RetryOnConflict``."""

    return await on_error(
        backoff, is_conflict, fn, sleep_func, random_func)


async def on_retry_after_error(
    backoff: Backoff,
    retriable: Callable[[Exception], bool],
    fn: Callable[[], Awaitable[T]],
    sleep_func: Callable[[float], Awaitable[None]] = asyncio.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Async implementation of client-go REST Retry-After sleep semantics."""

    steps = backoff.steps
    duration = backoff.duration
    last_error = None
    while steps > 0:
        try:
            return await fn()
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
            await sleep_func(delay)

    raise last_error
