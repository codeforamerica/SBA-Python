#!/usr/bin/env python

"""Unit tests for Python API wrapper."""

import unittest

from mock import Mock

import api
from api import SBA_API

def set_up_tests():
    """Cut down on boilerplate setup testing code."""
    api.urlopen = Mock()
    api.json = Mock()


def called_url():
    """Test what URL was called through the mocked urlopen."""
    url = api.urlopen.call_args[0][0]
    return url


class Test_SBA_API(unittest.TestCase):

    def setUp(self):
        set_up_tests()

    def test_base_url(self):
        example = SBA_API()
        self.assertEquals(example.base_url, 'http://api.sba.gov')

class TestApiMethod(unittest.TestCase):

    def setUp(self):
        set_up_tests()

    def test_empty_api_method_fails(self):
        self.assertRaises(TypeError, SBA_API())

class TestExampleMethod(unittest.TestCase):

    def setUp(self):
        set_up_tests()

    def test_(self):
        SBA_API().example()
        url = called_url()
        expected_url = ('http://something.web/'
                        'example?api_key=fake_api_key')
        self.assertEquals(url, expected_url)


if __name__ == '__main__':
    unittest.main()
