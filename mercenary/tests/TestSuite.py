__author__ = 'jeffstrickler - jeff@mercenarytech.com'


import json

import unittest
from tornado.httpclient import *


class TestTrie(unittest.TestCase):

    """
    def test_load(self):
        print "test_load"
        try:
            request = HTTPRequest(url="http://localhost:7777/load",connect_timeout=20.0, method="GET")
            http = HTTPClient()

            response = http.fetch(request)
            self.assertTrue(response.code == 200)

        except Exception as http_exception:
            print http_exception
    """


    def test_add(self):
        print "test_add"
        try:
            request = HTTPRequest(url="http://localhost:7777/add/foo",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

            request = HTTPRequest(url="http://localhost:7777/add/foobar",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

            request = HTTPRequest(url="http://localhost:7777/add/foodie",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

            request = HTTPRequest(url="http://localhost:7777/add/fool",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

            request = HTTPRequest(url="http://localhost:7777/add/fred",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

            request = HTTPRequest(url="http://localhost:7777/add/alice",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

            request = HTTPRequest(url="http://localhost:7777/add/mary",connect_timeout=20.0, method="GET")
            http = HTTPClient()
            response = http.fetch(request)
            self.assertTrue(response.code == 200)

        except Exception as http_exception:
            print http_exception

    def test_count(self):
        print "test_count"
        try:
            request = HTTPRequest(url="http://localhost:7777/count",connect_timeout=20.0, method="GET")
            http = HTTPClient()

            response = http.fetch(request)
            self.assertTrue(json.loads(response.body) >0)

        except Exception as http_exception:
            print http_exception


    def test_all(self):
        print "test_all"
        try:
            request = HTTPRequest(url="http://localhost:7777/all",connect_timeout=20.0, method="GET")
            http = HTTPClient()

            response = http.fetch(request)
            self.assertIsNotNone(json.loads(response.body))

        except Exception as http_exception:
            print http_exception

    def test_exists(self):
        print "test_exists"
        try:
            request = HTTPRequest(url="http://localhost:7777/exists/alice",connect_timeout=20.0, method="GET")
            http = HTTPClient()

            response = http.fetch(request)
            self.assertTrue(json.loads(response.body))

        except Exception as http_exception:
            print http_exception

    def test_contains(self):
        print "test_contains"
        try:
            request = HTTPRequest(url="http://localhost:7777/contains/fo",connect_timeout=20.0, method="GET")
            http = HTTPClient()

            response = http.fetch(request)
            self.assertIsNotNone(json.loads(response.body))

        except Exception as http_exception:
            print http_exception


    def setUp(self):
        print "setUp"
        pass


    def tearDown(self):
        print "tearDown"
        pass


suite = unittest.TestLoader().loadTestsFromTestCase(TestTrie)
unittest.TextTestRunner(verbosity=2).run(suite)