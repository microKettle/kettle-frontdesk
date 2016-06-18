#!flask/bin/python
import app
import unittest


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        app.instance.config['TESTING'] = True
        self.app = app.instance.test_client()


    def testSignIn(self):
        rv = self.app.post('/auth/sign_in')
        assert b'Sign In' in rv.data

    def testSignOut(self):
        rv = self.app.post('/auth/sign_out')
        assert b'Sign Out' in rv.data

if __name__ == '__main__':
    unittest.main()
