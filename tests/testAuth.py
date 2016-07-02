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


    def testUserReadSuccess(self):
        user = app.models.user.User.create({
            'name': 'John Staff', 
            'email': 'johnstaff@example.com', 
            'firstName': 'John', 
            'lastName': 'Staff', 
            'address': '439 Guerrero Street, CA 94110 US', 
            'birthdate': '2015-06-22', 
            'frontdeskId': 1, 
            'frontdeskToken': 'abc123'
        })
        response = self.app.get('/v1/users/' + str(user.resource_id));
        assert response.status_code == 200
        data = json.loads(response.data.decode('utf-8'));
        assert 'id' in data['user']
        assert data['user']['name'] == 'John Staff'
        assert data['user']['email'] == 'johnstaff@example.com'
        assert data['user']['firstName'] == 'John'
        assert data['user']['lastName'] == 'Staff'
        assert data['user']['address'] == '439 Guerrero Street, CA 94110 US'
        assert data['user']['birthdate'] == '2015-06-22'
        assert data['user']['frontdeskId'] == 1
        assert data['user']['frontdeskToken'] == 'abc123'


    def testUserReadNotFound(self):
        response = self.app.get('/users/234');
        assert response.status_code == 404


    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    @unittest.mock.patch('app.services.frontdesk.get_user_info')
    def testUserCreateSuccess(self, get_user_info, get_access_token):
        get_access_token.return_value = 'abc123'
        get_user_info.return_value = {
            "name": "John Staff",
            "email": "johnstaff@example.com",
            "firstName": "John",
            "middleName": None,
            "lastName": "Staff",
            "address": "400 Broad St, Seattle, WA 98109",
            "birthdate": "1980-01-01",
            "frontdeskId": 1
        }

        payload = {
           'user': {
                'temporaryToken': 'axyz789'
           }
        }
        response = self.app.post('/v1/users', data=json.dumps(payload));
        user = app.models.user.User.objects.get(frontdeskId=1)
        assert response.status_code == 201
        assert user.name == get_user_info.return_value['name']
        assert user.address == get_user_info.return_value['address']

    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    def testUserCreateInvalidTemporaryToken(self, get_access_token):
        get_access_token.return_value = False
        
        payload = {
           'user': {
                'temporaryToken': 'axyz789'
           }
        }
        response = self.app.post('/v1/users', data=json.dumps(payload));
        assert response.status_code == 400

    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    def testUserCreateRequestMalformed(self, get_access_token):
        get_access_token.return_value = False

        payload = {
            'temporaryToken': 'axyz789'
        }
        response = self.app.post('/users', data=json.dumps(payload));
        assert response.status_code == 422


    @unittest.mock.patch('app.services.frontdesk.get_access_token')
    @unittest.mock.patch('app.services.frontdesk.get_user_info')
    def testUserCreateAlreadyRegistered(self, get_user_info, get_access_token):        
        get_access_token.return_value = 'def456'
        get_user_info.return_value = {
            "frontdeskId": 1,
            "name": "Jack Doe",
            "email": "jackdoe@example.com",
            "firstName": "Jack",
            "middleName": None,
            "lastName": "Doe",
            "address": "419 Guerrero Street, San Franciscp, CA 91114",
            "birthdate": "1988-04-05"
        }

        payload = {
           'user': {
                'temporaryToken': 'axyz789'
           }
        }

        user = app.models.user.User.create({
            'name': 'John Staff', 
            'email': 'johnstaff@example.com', 
            'firstName': 'John', 
            'lastName': 'Staff', 
            'address': '439 Guerrero Street, CA 94110 US', 
            'birthdate': '2015-06-22', 
            'frontdeskId': 1, 
            'frontdeskToken': 'abc123'
        })

        response = response = self.app.post('/users', data=json.dumps(payload));
        user = app.models.user.User.find_by('frontdeskId', get_user_info.return_value['frontdeskId'])
        assert response.status_code == 201
        assert user.frontdeskToken ==  get_access_token.return_value
        assert user.name == get_user_info.return_value['name']
        assert user.email == get_user_info.return_value['email']


if __name__ == '__main__':
    unittest.main()
