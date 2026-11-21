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

import datetime
import unittest

from pydantic import BaseModel, ValidationError

from kubernetes.client import ApiClient
from kubernetes.utils import Duration


class Spec(BaseModel):
    ttl: Duration


class DurationTest(unittest.TestCase):

    def test_parses_go_durations(self):
        cases = {
            "720h0m0s": datetime.timedelta(hours=720),
            "1h30m": datetime.timedelta(minutes=90),
            "1.5s": datetime.timedelta(seconds=1.5),
            "500ms": datetime.timedelta(milliseconds=500),
            "1us": datetime.timedelta(microseconds=1),
            "1\u00b5s": datetime.timedelta(microseconds=1),
            ".5s": datetime.timedelta(milliseconds=500),
            "+5s": datetime.timedelta(seconds=5),
            "0": datetime.timedelta(0),
            "0s": datetime.timedelta(0),
            "-1h": datetime.timedelta(hours=-1),
        }
        for value, expected in cases.items():
            with self.subTest(value=value):
                self.assertEqual(expected, Spec(ttl=value).ttl)

    def test_accepts_timedelta(self):
        ttl = datetime.timedelta(minutes=5)
        self.assertEqual(ttl, Spec(ttl=ttl).ttl)

    def test_dumps_go_durations(self):
        cases = {
            datetime.timedelta(hours=720): "720h0m0s",
            datetime.timedelta(hours=10 ** 6): "1000000h0m0s",
            datetime.timedelta(minutes=90): "1h30m0s",
            datetime.timedelta(seconds=90): "1m30s",
            datetime.timedelta(seconds=1.5): "1.5s",
            datetime.timedelta(seconds=59, microseconds=123456): "59.123456s",
            datetime.timedelta(minutes=10, microseconds=1): "10m0.000001s",
            datetime.timedelta(milliseconds=1.5): "1.5ms",
            datetime.timedelta(microseconds=1): "1us",
            datetime.timedelta(minutes=-90): "-1h30m0s",
            datetime.timedelta(0): "0s",
        }
        for ttl, expected in cases.items():
            with self.subTest(ttl=ttl):
                self.assertEqual({"ttl": expected}, Spec(ttl=ttl).model_dump())
                self.assertEqual('{"ttl":"%s"}' % expected,
                                 Spec(ttl=ttl).model_dump_json())

    def test_json_round_trip(self):
        spec = Spec(ttl="2m30.5s")
        self.assertEqual(spec, Spec.model_validate_json(spec.model_dump_json()))

    def test_rejects_invalid_durations(self):
        for value in ["abc", "1", "1x", "", "1d", "1h 2m", "1h-2m", "2562048h",
                      "\u0661s", "99999999999h", "1" + "0" * 310 + "h"]:
            with self.subTest(value=value):
                with self.assertRaises(ValidationError):
                    Spec(ttl=value)

    def test_rejects_out_of_range_timedelta(self):
        with self.assertRaises(ValidationError):
            Spec(ttl=datetime.timedelta(hours=2562048))

    def test_dumped_model_is_a_valid_request_body(self):
        body = ApiClient().sanitize_for_serialization(
            Spec(ttl="720h0m0s").model_dump())
        self.assertEqual({"ttl": "720h0m0s"}, body)


if __name__ == '__main__':
    unittest.main()
