#!/usr/bin/env python3
""" mock and parameterized unittest on utils.py access_nested_map class. """
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """tests the access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """check if access_nested_map function returns correct output """
        correct _output = access_nested_map(map, path)
        self.assertEqual(correct_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """raises an exception if access_nested_map has a key error"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """tests the get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """checks if get_json function returns correct output """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            correct_response = get_json(test_url)
            self.assertEqual(correct_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """tests for memoization """

    def test_memoize(self):
        """tests the memoize function decorator"""

        class TestClass:
            """test class """

            def a_method(self):
                """returns 42 """
                return 42

            @memoize
            def a_property(self):
                """returns a memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            memo = TestClass()
            memo.a_property
            memo.a_property
            mocked.asset_called_once()
