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

import unittest

from kubernetes.aio.utils.retry import (
    Backoff,
    DEFAULT_RETRY,
    is_too_many_requests,
    on_error,
    on_retry_after_error,
    retry_after_seconds,
    retry_on_conflict,
)


class FakeError(Exception):

    def __init__(self, status, headers=None):
        super().__init__("status {0}".format(status))
        self.status = status
        self.headers = headers or {}


class AioRetryTest(unittest.IsolatedAsyncioTestCase):

    def test_default_retry_matches_client_go(self):
        self.assertEqual(
            DEFAULT_RETRY,
            Backoff(steps=5, duration=0.01, factor=1.0, jitter=0.1),
        )

    def test_retry_after_seconds_parses_delay_seconds(self):
        error = FakeError(429, {"Retry-After": "7"})

        self.assertEqual(retry_after_seconds(error), 7.0)

    async def test_on_error_retries_retriable_errors(self):
        attempts = []
        sleeps = []

        async def fn():
            attempts.append(1)
            if len(attempts) < 3:
                raise FakeError(500)
            return "ok"

        async def sleep(delay):
            sleeps.append(delay)

        result = await on_error(
            Backoff(steps=4, duration=1.0, factor=2.0),
            lambda e: getattr(e, "status", None) == 500,
            fn,
            sleep_func=sleep,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(len(attempts), 3)
        self.assertEqual(sleeps, [1.0, 2.0])

    async def test_on_retry_after_error_honors_retry_after_for_429(self):
        attempts = []
        sleeps = []

        async def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise FakeError(429, {"Retry-After": "3"})
            return "ok"

        async def sleep(delay):
            sleeps.append(delay)

        result = await on_retry_after_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            is_too_many_requests,
            fn,
            sleep_func=sleep,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [3.0])

    async def test_retry_on_conflict_retries(self):
        attempts = []
        sleeps = []

        async def fn():
            attempts.append(1)
            if len(attempts) < 3:
                raise FakeError(409)
            return "updated"

        async def sleep(delay):
            sleeps.append(delay)

        result = await retry_on_conflict(
            fn,
            backoff=Backoff(steps=3, duration=1.0, factor=1.0),
            sleep_func=sleep,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "updated")
        self.assertEqual(len(attempts), 3)
        self.assertEqual(sleeps, [1.0, 1.0])


if __name__ == "__main__":
    unittest.main()
