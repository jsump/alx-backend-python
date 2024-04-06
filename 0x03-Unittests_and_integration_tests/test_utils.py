#!/usr/bin/env python3
"""
Module: test_utils.py

First unit test for utils.access_nested_map
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TesteAcessNestedMap(unittest.TestCase):
    """
    This class contains the unit testst
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test for expected result
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
