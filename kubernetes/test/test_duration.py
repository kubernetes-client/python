import unittest
import datetime

import kubernetes
from kubernetes.utils.duration import parse_duration, format_duration

class TestDuration(unittest.TestCase):

    def test_parse_duration(self):
        # Valid durations
        self.assertEqual(parse_duration("0h"), datetime.timedelta(hours=0))
        self.assertEqual(parse_duration("0s"), datetime.timedelta(hours=0))
        self.assertEqual(parse_duration("0h0m0s"), datetime.timedelta(hours=0))
        self.assertEqual(parse_duration("1h"), datetime.timedelta(hours=1))
        self.assertEqual(parse_duration("30m"), datetime.timedelta(minutes=30))
        self.assertEqual(parse_duration("10s"), datetime.timedelta(seconds=10))
        self.assertEqual(parse_duration("500ms"), datetime.timedelta(milliseconds=500))
        self.assertEqual(parse_duration("2h30m"), datetime.timedelta(hours=2, minutes=30))
        self.assertEqual(parse_duration("150m"), datetime.timedelta(hours=2, minutes=30))
        self.assertEqual(parse_duration("7230s"), datetime.timedelta(hours=2, seconds=30))
        self.assertEqual(parse_duration("1h30m10s"), datetime.timedelta(hours=1, minutes=30, seconds=10))
        self.assertEqual(parse_duration("10s30m1h"), datetime.timedelta(hours=1, minutes=30, seconds=10))
        self.assertEqual(parse_duration("100ms200ms300ms"), datetime.timedelta(milliseconds=600))
        self.assertEqual(parse_duration("100ms200ms300ms"), datetime.timedelta(milliseconds=600))

        # Invalid durations
        with self.assertRaises(ValueError):
            parse_duration("1d")  # Invalid unit 'd'
        with self.assertRaises(ValueError):
            parse_duration("1")  # Missing unit
        with self.assertRaises(ValueError):
            parse_duration("1m1")  # Missing unit
        with self.assertRaises(ValueError):
            parse_duration("1h30m10s20ms50h")  # Too many units
        with self.assertRaises(ValueError):
            parse_duration("999999h")  # Too many digits
        with self.assertRaises(ValueError):
            parse_duration("1.5h")  # Floating point is not supported
        with self.assertRaises(ValueError):
            parse_duration("-15m")  # Negative durations are not supported

    def test_format_duration(self):
        # Valid durations
        self.assertEqual(format_duration(datetime.timedelta(0)), "0s")
        self.assertEqual(format_duration(datetime.timedelta(hours=1)), "1h")
        self.assertEqual(format_duration(datetime.timedelta(minutes=30)), "30m")
        self.assertEqual(format_duration(datetime.timedelta(seconds=10)), "10s")
        self.assertEqual(format_duration(datetime.timedelta(milliseconds=500)), "500ms")
        self.assertEqual(format_duration(datetime.timedelta(hours=2, minutes=30)), "2h30m")
        self.assertEqual(format_duration(datetime.timedelta(hours=1, minutes=30, seconds=10)), "1h30m10s")
        self.assertEqual(format_duration(datetime.timedelta(milliseconds=600)), "600ms")
        self.assertEqual(format_duration(datetime.timedelta(hours=2, milliseconds=600)), "2h600ms")
        self.assertEqual(format_duration(datetime.timedelta(hours=2, minutes=30, milliseconds=600)), "2h30m600ms")
        self.assertEqual(format_duration(datetime.timedelta(hours=2, minutes=30, seconds=10, milliseconds=600)), "2h30m10s600ms")
        self.assertEqual(format_duration(datetime.timedelta(minutes=0.5)), "30s")
        self.assertEqual(format_duration(datetime.timedelta(seconds=0.5)), "500ms")
        self.assertEqual(format_duration(datetime.timedelta(days=10)), "240h")  # 10 days = 240 hours

        # Invalid durations
        with self.assertRaises(ValueError):
            format_duration(datetime.timedelta(microseconds=100))  # Sub-millisecond precision
        with self.assertRaises(ValueError):
            format_duration(datetime.timedelta(milliseconds=0.5))  # Sub-millisecond precision
        with self.assertRaises(ValueError):
            format_duration(datetime.timedelta(days=10000))  # Out of range (more than 99999 hours)
        with self.assertRaises(ValueError):
            format_duration(datetime.timedelta(minutes=-15))  # Negative durations are not supported

if __name__ == '__main__':
    unittest.main()