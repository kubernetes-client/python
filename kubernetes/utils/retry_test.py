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

from kubernetes.client.exceptions import ApiException
from kubernetes.utils.retry import (
    Backoff,
    DEFAULT_BACKOFF,
    DEFAULT_RETRY,
    DEFAULT_RETRY_AFTER_BACKOFF,
    is_conflict,
    is_retry_after_response,
    is_too_many_requests,
    on_error,
    on_retry_after_error,
    retry_after_backoff,
    retry_after_max_retries,
    retry_on_conflict,
    retry_after_seconds,
)
from urllib3.util.retry import Retry


def api_exception(status, headers=None):
    error = ApiException(status=status)
    error.headers = headers or {}
    return error


class RetryTest(unittest.TestCase):

    def test_default_backoffs_match_client_go(self):
        self.assertEqual(
            DEFAULT_BACKOFF,
            Backoff(steps=4, duration=0.01, factor=5.0, jitter=0.1),
        )
        self.assertEqual(
            DEFAULT_RETRY,
            Backoff(steps=5, duration=0.01, factor=1.0, jitter=0.1),
        )
        self.assertEqual(
            DEFAULT_RETRY_AFTER_BACKOFF,
            Backoff(steps=11, duration=0.0, factor=1.0, jitter=0.0),
        )

    def test_retry_after_backoff_uses_configuration_retries(self):
        self.assertEqual(retry_after_max_retries(None), 10)
        self.assertEqual(retry_after_max_retries(False), 0)
        self.assertEqual(retry_after_max_retries(0), 0)
        self.assertEqual(retry_after_max_retries(3), 3)
        self.assertEqual(retry_after_max_retries(Retry(total=2)), 2)
        self.assertEqual(retry_after_backoff(3).steps, 4)

    def test_retry_after_backoff_can_be_configured(self):
        configured = Backoff(
            steps=4, duration=1.0, factor=2.0, jitter=0.3, cap=5.0)

        self.assertEqual(retry_after_backoff(None, configured), configured)
        self.assertEqual(
            retry_after_backoff(1, configured),
            Backoff(
                steps=2, duration=1.0, factor=2.0, jitter=0.3, cap=5.0),
        )

    def test_on_error_returns_without_retry(self):
        attempts = []

        def fn():
            attempts.append(1)
            return "ok"

        result = on_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            lambda e: True,
            fn,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(len(attempts), 1)

    def test_on_error_retries_retriable_errors(self):
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            if len(attempts) < 3:
                raise api_exception(500)
            return "ok"

        result = on_error(
            Backoff(steps=4, duration=1.0, factor=2.0),
            lambda e: getattr(e, "status", None) == 500,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(len(attempts), 3)
        self.assertEqual(sleeps, [1.0, 2.0])

    def test_on_error_exhausts_retries(self):
        test_error = api_exception(500)
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            raise test_error

        with self.assertRaises(ApiException) as ctx:
            on_error(
                Backoff(steps=3, duration=1.0, factor=2.0),
                lambda e: getattr(e, "status", None) == 500,
                fn,
                sleep_func=sleeps.append,
                random_func=lambda: 0.0,
            )

        self.assertIs(ctx.exception, test_error)
        self.assertEqual(len(attempts), 3)
        self.assertEqual(sleeps, [1.0, 2.0])

    def test_on_error_raises_non_retriable_error(self):
        sleeps = []

        def fn():
            raise api_exception(400)

        with self.assertRaises(ApiException) as ctx:
            on_error(
                Backoff(steps=3, duration=1.0, factor=2.0),
                lambda e: getattr(e, "status", None) == 500,
                fn,
                sleep_func=sleeps.append,
            )

        self.assertEqual(ctx.exception.status, 400)
        self.assertEqual(sleeps, [])

    def test_on_error_applies_jitter(self):
        sleeps = []
        attempts = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(500)
            return "ok"

        result = on_error(
            Backoff(steps=2, duration=10.0, factor=1.0, jitter=0.5),
            lambda e: getattr(e, "status", None) == 500,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.25,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [11.25])

    def test_on_error_keeps_duration_when_factor_is_zero(self):
        sleeps = []
        attempts = []

        def fn():
            attempts.append(1)
            if len(attempts) < 3:
                raise api_exception(500)
            return "ok"

        result = on_error(
            Backoff(steps=3, duration=1.0, factor=0.0),
            lambda e: getattr(e, "status", None) == 500,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [1.0, 1.0])

    def test_backoff_rejects_invalid_values(self):
        with self.assertRaises(ValueError):
            Backoff(steps=0, duration=1.0, factor=1.0)
        with self.assertRaises(ValueError):
            Backoff(steps=1, duration=-1.0, factor=1.0)
        with self.assertRaises(ValueError):
            Backoff(steps=1, duration=1.0, factor=-1.0)
        with self.assertRaises(ValueError):
            Backoff(steps=1, duration=1.0, factor=1.0, jitter=-1.0)
        with self.assertRaises(ValueError):
            Backoff(steps=1, duration=1.0, factor=1.0, cap=-1.0)

    def test_on_error_stops_after_capped_sleep(self):
        test_error = api_exception(500)
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            raise test_error

        with self.assertRaises(ApiException) as ctx:
            on_error(
                Backoff(steps=4, duration=1.0, factor=5.0, cap=3.0),
                lambda e: getattr(e, "status", None) == 500,
                fn,
                sleep_func=sleeps.append,
                random_func=lambda: 0.0,
            )

        self.assertIs(ctx.exception, test_error)
        self.assertEqual(len(attempts), 1)
        self.assertEqual(sleeps, [1.0])

    def test_retry_on_conflict_never_returns(self):
        conflict_error = api_exception(409)

        def fn():
            raise conflict_error

        with self.assertRaises(ApiException) as ctx:
            retry_on_conflict(
                fn,
                backoff=Backoff(steps=3, duration=0.0, factor=1.0),
                sleep_func=lambda delay: None,
                random_func=lambda: 0.0,
            )

        self.assertIs(ctx.exception, conflict_error)

    def test_retry_on_conflict_returns_immediately(self):
        attempts = []

        def fn():
            attempts.append(1)
            return "updated"

        result = retry_on_conflict(
            fn,
            backoff=Backoff(steps=3, duration=0.0, factor=1.0),
        )

        self.assertEqual(result, "updated")
        self.assertEqual(len(attempts), 1)

    def test_retry_on_conflict_returns_immediately_on_non_conflict(self):
        test_error = api_exception(500)

        def fn():
            raise test_error

        with self.assertRaises(ApiException) as ctx:
            retry_on_conflict(
                fn,
                backoff=Backoff(steps=3, duration=0.0, factor=1.0),
            )

        self.assertIs(ctx.exception, test_error)

    def test_retry_on_conflict_keeps_retrying(self):
        attempts = []
        sleeps = []

        def fn():
            if len(attempts) < 2:
                attempts.append(1)
                raise api_exception(409)
            return "updated"

        result = retry_on_conflict(
            fn,
            backoff=Backoff(steps=3, duration=1.0, factor=1.0),
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "updated")
        self.assertEqual(len(attempts), 2)
        self.assertEqual(sleeps, [1.0, 1.0])

    def test_retry_after_seconds_parses_delay_seconds(self):
        error = api_exception(429, {"Retry-After": "7"})

        self.assertEqual(retry_after_seconds(error), 7.0)

    def test_retry_after_seconds_rejects_http_date(self):
        error = api_exception(
            429,
            {"retry-after": "Wed, 21 Oct 2015 07:28:00 GMT"},
        )

        self.assertIsNone(retry_after_seconds(error))

    def test_retry_after_seconds_returns_none_without_header(self):
        self.assertIsNone(retry_after_seconds(api_exception(429)))

    def test_retry_after_seconds_returns_none_for_invalid_header(self):
        error = api_exception(429, {"Retry-After": "invalid"})

        self.assertIsNone(retry_after_seconds(error))

    def test_retry_after_seconds_rejects_float_values(self):
        error = api_exception(429, {"Retry-After": "0.5"})

        self.assertIsNone(retry_after_seconds(error))

    def test_on_error_uses_backoff_with_retry_after(self):
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(429, {"Retry-After": "3"})
            return "ok"

        result = on_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            is_too_many_requests,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [1.0])

    def test_on_retry_after_error_honors_retry_after_for_429(self):
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(429, {"Retry-After": "3"})
            return "ok"

        result = on_retry_after_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            is_too_many_requests,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [3.0])

    def test_on_retry_after_error_uses_backoff_when_longer(self):
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(429, {"Retry-After": "1"})
            return "ok"

        result = on_retry_after_error(
            Backoff(steps=3, duration=3.0, factor=2.0),
            is_too_many_requests,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [3.0])

    def test_on_retry_after_error_honors_retry_after_for_5xx(self):
        attempts = []
        sleeps = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(500, {"Retry-After": "3"})
            return "ok"

        result = on_retry_after_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            lambda e: getattr(e, "status", None) == 500,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [3.0])

    def test_on_retry_after_error_falls_back_without_retry_after(self):
        sleeps = []
        attempts = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(429)
            return "ok"

        result = on_retry_after_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            is_too_many_requests,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [1.0])

    def test_on_retry_after_error_falls_back_with_invalid_retry_after(self):
        sleeps = []
        attempts = []

        def fn():
            attempts.append(1)
            if len(attempts) < 2:
                raise api_exception(429, {"Retry-After": "invalid"})
            return "ok"

        result = on_retry_after_error(
            Backoff(steps=3, duration=1.0, factor=2.0),
            is_too_many_requests,
            fn,
            sleep_func=sleeps.append,
            random_func=lambda: 0.0,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(sleeps, [1.0])

    def test_retry_after_seconds_rejects_negative_values(self):
        error = api_exception(429, {"Retry-After": "-1"})

        self.assertIsNone(retry_after_seconds(error))

    def test_status_helpers(self):
        self.assertTrue(is_conflict(api_exception(409)))
        self.assertFalse(is_conflict(api_exception(500)))
        self.assertTrue(is_too_many_requests(api_exception(429)))
        self.assertFalse(is_too_many_requests(api_exception(409)))
        self.assertTrue(
            is_retry_after_response(
                api_exception(429, {"Retry-After": "1"})))
        self.assertTrue(
            is_retry_after_response(
                api_exception(500, {"Retry-After": "1"})))
        self.assertFalse(is_retry_after_response(api_exception(429)))
        self.assertFalse(
            is_retry_after_response(
                api_exception(500, {"Retry-After": "invalid"})))
        self.assertFalse(
            is_retry_after_response(
                api_exception(409, {"Retry-After": "1"})))


if __name__ == "__main__":
    unittest.main()
