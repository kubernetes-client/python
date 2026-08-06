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
    _delay,
    is_retry_after_response,
    retry_after_backoff,
    retry_after_seconds,
)


T = TypeVar("T")


def on_retry_after_error(
    backoff: Backoff,
    retriable: Callable[[Exception], bool],
    fn: Callable[[], T],
    sleep_func: Callable[[float], None] = time.sleep,
    random_func: Callable[[], float] = random.random,
) -> T:
    """Run ``fn`` with client-go REST Retry-After sleep semantics."""

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
