#!flask/bin/python
from hello import app
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()



    def test_empty_db(self):
        rv = self.app.get('/')
        assert b'Hello' in rv.data

if __name__ == '__main__':
    unittest.main()
