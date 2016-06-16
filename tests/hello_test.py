#!flask/bin/python
from app.app import app
import unittest


class HelloTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()



    def testRoot(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data

if __name__ == '__main__':
    unittest.main()
