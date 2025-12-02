# Copyright 2016 The Kubernetes Authors.
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
from datetime import datetime

from .dateutil import UTC, TimezoneInfo, format_rfc3339, parse_rfc3339


class DateUtilTest(unittest.TestCase):

    def _parse_rfc3339_test(self, st, y, m, d, h, mn, s, us):
        actual = parse_rfc3339(st)
        expected = datetime(y, m, d, h, mn, s, us, UTC)
        self.assertEqual(expected, actual)

    def test_parse_rfc3339(self):
        self._parse_rfc3339_test("2017-07-25T04:44:21Z",
                                 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25 04:44:21Z",
                                 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21",
                                 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21z",
                                 2017, 7, 25, 4, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21+03:00",
                                 2017, 7, 25, 1, 44, 21, 0)
        self._parse_rfc3339_test("2017-07-25T04:44:21-03:00",
                                 2017, 7, 25, 7, 44, 21, 0)

        self._parse_rfc3339_test("2017-07-25T04:44:21,005Z",
                                 2017, 7, 25, 4, 44, 21, 5000)
        self._parse_rfc3339_test("2017-07-25T04:44:21.005Z",
                                 2017, 7, 25, 4, 44, 21, 5000)
        self._parse_rfc3339_test("2017-07-25 04:44:21.0050Z",
                                 2017, 7, 25, 4, 44, 21, 5000)
        self._parse_rfc3339_test("2017-07-25T04:44:21.5",
                                 2017, 7, 25, 4, 44, 21, 500000)
        self._parse_rfc3339_test("2017-07-25T04:44:21.005z",
                                 2017, 7, 25, 4, 44, 21, 5000)
        self._parse_rfc3339_test("2017-07-25T04:44:21.005+03:00",
                                 2017, 7, 25, 1, 44, 21, 5000)
        self._parse_rfc3339_test("2017-07-25T04:44:21.005-03:00",
                                 2017, 7, 25, 7, 44, 21, 5000)

    def test_format_rfc3339(self):
        self.assertEqual(
            format_rfc3339(datetime(2017, 7, 25, 4, 44, 21, 0, UTC)),
            "2017-07-25T04:44:21Z")
        self.assertEqual(
            format_rfc3339(datetime(2017, 7, 25, 4, 44, 21, 0,
                                    TimezoneInfo(2, 0))),
            "2017-07-25T02:44:21Z")
        self.assertEqual(
            format_rfc3339(datetime(2017, 7, 25, 4, 44, 21, 0,
                                    TimezoneInfo(-2, 30))),
            "2017-07-25T07:14:21Z")

    def test_parse_rfc3339_invalid_formats(self):
        """Test that invalid RFC3339 formats raise ValueError"""
        invalid_inputs = [
            "2025-13-02T13:37:00Z",        # Invalid month
            "2025-12-32T13:37:00Z",        # Invalid day
            "2025-12-02T25:00:00Z",        # Invalid hour
            "2025-12-02T13:60:00Z",        # Invalid minute
            "2025-12-02T13:37:60Z",        # Invalid second
            "not-a-valid-date",            # Completely invalid
            "",                             # Empty string
            "2025-12-02Z13:37:00",         # Timezone before time
        ]

        for invalid_input in invalid_inputs:
            with self.assertRaises(ValueError):
                parse_rfc3339(invalid_input)



    def test_parse_rfc3339_with_whitespace(self):
        """Test that leading/trailing whitespace is handled"""
        actual = parse_rfc3339("  2017-07-25T04:44:21Z  ")
        expected = datetime(2017, 7, 25, 4, 44, 21, 0, UTC)
        self.assertEqual(expected, actual)

    def test_parse_rfc3339_error_message_clarity(self):
        """Test that error messages are clear and helpful"""
        try:
            parse_rfc3339("invalid-date-format")
        except ValueError as e:
            error_msg = str(e)
            # Verify error message contains helpful information
            self.assertIn("Invalid RFC3339", error_msg)
            self.assertIn("YYYY-MM-DD", error_msg)
            self.assertIn("expected", error_msg)
