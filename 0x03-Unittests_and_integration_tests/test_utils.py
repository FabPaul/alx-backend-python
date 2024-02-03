#!/usr/bin/env python3
"""
In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test
that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function
for following inputs:
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import Mock, patch
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unittest class that inherits from access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Tests"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, exp_result):
        """Tests"""
        with self.assertRaises(exp_result) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class to test that utils.get_json returns the expected results"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected_result):
        """Tests"""
        mock = Mock()
        mock.json.return_value = expected_result
        with patch('requests.get', return_value=mock):
            response = get_json(url)
            self.assertEqual(response, expected_result)
