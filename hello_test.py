#!flask/bin/python
from hello import app
import unittest


class HelloTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()



    def getRoot(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data

if __name__ == '__main__':
    unittest.main()
