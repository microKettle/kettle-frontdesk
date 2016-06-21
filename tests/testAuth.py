#!flask/bin/python
import app
import app.models.user
import app.services.frontdesk
import json
import unittest
import unittest.mock


class AuthTestCase(unittest.TestCase):

    def setUp(self):
        app.instance.config['TESTING'] = True
        self.app = app.instance.test_client()

    def tearDown(self):
        app.models.user.User.drop_collection()

    def testSignIn(self):
        rv = self.app.post('/auth/sign_in')
        assert b'Sign In' in rv.data

    def testSignOut(self):
        rv = self.app.post('/auth/sign_out')
        assert b'Sign Out' in rv.data

    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    @unittest.mock.patch('app.services.frontdesk.get_user_info')
    def testCallbackSuccess(self, get_user_info, get_access_token):
        get_access_token.return_value = 'abc123'
        get_user_info.return_value = {
            "id": 1,
            "name": "John Staff",
            "email": "johnstaff@example.com",
            "first_name": "John",
            "middle_name": None,
            "last_name": "Staff",
            "address": "400 Broad St, Seattle, WA 98109",
            "secondary_info_field": "Unlimited Membership",
            "birthdate": "1980-01-01"
        }
        
        rv = self.app.get('/auth/callback?code=toto')
        assert rv.status_code == 204
        user = app.models.user.User.objects.get(frontdesk_id=1)
        assert user.access_token == 'abc123'
        assert user.name == 'John Staff'
        assert user.email == "johnstaff@example.com"

    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    @unittest.mock.patch('app.services.frontdesk.get_user_info')
    def testCallBackUserAlreadyRegistered(self, get_user_info, get_access_token):        
        get_access_token.return_value = 'def456'
        get_user_info.return_value = {
            "id": 1,
            "name": "Jack Doe",
            "email": "jackdoe@example.com",
            "first_name": "Jack",
            "middle_name": None,
            "last_name": "Doe",
            "address": "419 Guerrero Street, San Franciscp, CA 91114",
            "secondary_info_field": "Unlimited Membership",
            "birthdate": "1988-04-05"
        }

        user = app.models.user.User(frontdesk_id=1, name='John Staff', email='johnstaff@example.com', access_token='abc123')
        user.save()
        rv = self.app.get('/auth/callback?code=toto')
        assert rv.status_code == 204

        user = app.models.user.User.objects.get(frontdesk_id=1)
        assert user.access_token == 'def456'
        assert user.name == 'Jack Doe'
        assert user.email == "jackdoe@example.com"

    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    def testCallBackInvalidTemporaryCode(self, get_access_token):        
        get_access_token.return_value = False
        rv = self.app.get('/auth/callback?code=toto')
        assert rv.status_code == 401

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
