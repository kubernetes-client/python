# coding: utf-8
# Copyright 2019 The Kubernetes Authors.
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

from __future__ import absolute_import

import unittest
from kubernetes.utils import parse_quantity
from decimal import Decimal


class TestQuantity(unittest.TestCase):
    def test_parse(self):
        self.assertIsInstance(parse_quantity(2.2), Decimal)
        # input, expected output
        tests = [
            (0, 0),
            (2, 2),
            (2, Decimal("2")),
            (2., 2),
            (Decimal("2.2"), Decimal("2.2")),
            (2., Decimal(2)),
            (Decimal("2."), 2),
            ("123", 123),
            ("2", 2),
            ("2n", Decimal("2") * Decimal(1000)**-3),
            ("2u", Decimal("0.000002")),
            ("2m", Decimal("0.002")),
            ("0m", Decimal("0")),
            ("0M", Decimal("0")),
            ("223k", 223000),
            ("002M", 2 * 1000**2),
            ("2M", 2 * 1000**2),
            ("4123G", 4123 * 1000**3),
            ("2T", 2 * 1000**4),
            ("2P", 2 * 1000**5),
            ("2E", 2 * 1000**6),

            ("223Ki", 223 * 1024),
            ("002Mi", 2 * 1024**2),
            ("2Mi", 2 * 1024**2),
            ("2Gi", 2 * 1024**3),
            ("4123Gi", 4123 * 1024**3),
            ("2Ti", 2 * 1024**4),
            ("2Pi", 2 * 1024**5),
            ("2Ei", 2 * 1024**6),

            ("2.34n", Decimal("2.34") * Decimal(1000)**-3),
            ("2.34u", Decimal("2.34") * Decimal(1000)**-2),
            ("2.34m", Decimal("2.34") * Decimal(1000)**-1),
            ("2.34Ki", Decimal("2.34") * 1024),
            ("2.34", Decimal("2.34")),
            (".34", Decimal("0.34")),
            ("34.", 34),
            (".34M", Decimal("0.34") * 1000**2),

            ("2e2K", Decimal("2e2") * 1000),
            ("2e2Ki", Decimal("2e2") * 1024),
            ("2e-2Ki", Decimal("2e-2") * 1024),
            ("2.34E1", Decimal("2.34E1")),
            (".34e-2", Decimal("0.34e-2")),
        ]

        for inp, out in tests:
            self.assertEqual(parse_quantity(inp), out)
            if isinstance(inp, (int, float, Decimal)):
                self.assertEqual(parse_quantity(-1 * inp), -out)
            else:
                self.assertEqual(parse_quantity("-" + inp), -out)
                self.assertEqual(parse_quantity("+" + inp), out)

    def test_parse_invalid(self):
        self.assertRaises(ValueError, parse_quantity, [])
        self.assertRaises(ValueError, parse_quantity, "")
        self.assertRaises(ValueError, parse_quantity, "-")
        self.assertRaises(ValueError, parse_quantity, "i")
        self.assertRaises(ValueError, parse_quantity, "2i")
        self.assertRaises(ValueError, parse_quantity, "2mm")
        self.assertRaises(ValueError, parse_quantity, "2mmKi")
        self.assertRaises(ValueError, parse_quantity, "2KKi")
        self.assertRaises(ValueError, parse_quantity, "2e")
        self.assertRaises(ValueError, parse_quantity, "2.2i")
        self.assertRaises(ValueError, parse_quantity, "bla")
        self.assertRaises(ValueError, parse_quantity, "Ki")
        self.assertRaises(ValueError, parse_quantity, "M")
        self.assertRaises(ValueError, parse_quantity, "2ki")
        self.assertRaises(ValueError, parse_quantity, "2Ki ")
        self.assertRaises(ValueError, parse_quantity, "20Ki ")
        self.assertRaises(ValueError, parse_quantity, "20B")
        self.assertRaises(ValueError, parse_quantity, "20Bi")
        self.assertRaises(ValueError, parse_quantity, "20.2Bi")
        self.assertRaises(ValueError, parse_quantity, "2MiKi")
        self.assertRaises(ValueError, parse_quantity, "2MK")
        self.assertRaises(ValueError, parse_quantity, "2MKi")
        self.assertRaises(ValueError, parse_quantity, "234df")
        self.assertRaises(ValueError, parse_quantity, "df234")
        self.assertRaises(ValueError, parse_quantity, tuple())


if __name__ == '__main__':
    unittest.main()
