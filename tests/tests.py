"""
Tests for ingestion utilities.

To run tests execute 'docker-compose -f docker-compose.tests.yml up' at the root
directory of the project
"""


import unittest
from datetime import date
from utils import parse_log, is_get_request


sample_log = [
    'remote - - [24/Oct/1994:14:05:31 -0600] "GET 23.html HTTP/1.0" 200 3787', # Remote/pass
    'remote - - [24/Oct/1994:19:08:17 -0600] "GET 164.html HTTP/1.0" 404 -', # Remote/fail
    'local - - [11/Oct/1995:14:11:40 -0600] "GET 3.gif HTTP/1.0" 200 36403', # Local/pass
    'local - - [11/Oct/1995:14:11:45 -0600] "GET 11459.html HTTP/1.0" 404 -', # Local/fail
    'remote - - [23/Jan/1997:14:11:45 -0600] "POST 1959.html HTTP/1.0" 200 -', # Fake post request
]


class IsGetRequestTestCase(unittest.TestCase):
    def test_get_request(self):
        self.assertTrue(is_get_request(sample_log[0]))

    def test_post_request(self):
        self.assertFalse(is_get_request(sample_log[4]))


class ParseLogTestCase(unittest.TestCase):
    def test_remote_pass(self):
        day, status, source = parse_log(sample_log[0])
        self.assertEqual(status, '200')
        self.assertEqual(source, 'remote')
        self.assertEqual(day, date(year=1994, month=10, day=24))

    def test_remote_fail(self):
        day, status, source = parse_log(sample_log[1])
        self.assertEqual(status, '404')
        self.assertEqual(source, 'remote')
        self.assertEqual(day, date(year=1994, month=10, day=24))

    def test_local_pass(self):
        day, status, source = parse_log(sample_log[2])
        self.assertEqual(status, '200')
        self.assertEqual(source, 'local')
        self.assertEqual(day, date(year=1995, month=10, day=11))

    def test_local_fail(self):
        day, status, source = parse_log(sample_log[3])
        self.assertEqual(status, '404')
        self.assertEqual(source, 'local')
        self.assertEqual(day, date(year=1995, month=10, day=11))


if __name__ == '__main__':
    unittest.main()