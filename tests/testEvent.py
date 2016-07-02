import app.models.user
import app.services.frontdesk
import unittest
import unittest.mock

class EventTestCase(unittest.TestCase):
    def setUp(self):
        app.instance.config['TESTING'] = True
        self.app = app.instance.test_client()

    def tearDown(self):
        app.models.user.User.drop_collection()

    @unittest.mock.patch('app.services.frontdesk.get_event_info')
    def testEventReadSuccess(self, get_event_info):
    	get_event_info.return_value = {
	      "id": 262,
	      "event_id": 3,
	      "name": "Group Workout",
	      "description": "Ut omnis quibusdam porro qui laudantium maxime quidem.",
	      "service_id": 1,
	      "location_id": 1,
	      "start_at": "2014-09-12T16:00:00Z",
	      "end_at": "2014-09-12T18:00:00Z",
	      "url": "http://mybiz.frontdeskhq.com/e/262",
	      "timezone": "America/Los_Angeles",
	      "state": "active",
	      "full": False,
	      "capacity_remaining": 18,
	      "staff_members": [
	        {
	          "id": 1,
	          "name": "John Staff"
	        }
	      ]
	    }

    	app.models.user.User.create({
            'id': 12,
            'name': 'John Staff', 
            'email': 'johnstaff@example.com', 
            'firstName': 'John', 
            'lastName': 'Staff', 
            'address': '439 Guerrero Street, CA 94110 US', 
            'birthdate': '2015-06-22', 
            'frontdeskId': 1, 
            'frontdeskToken': 'abc123'
        })

    	response = self.app.get('/users/12/events/7');
    	assert response.status_code == 200

    def testEventReadUserNotFound(self):
    	pass

    def testEventReadEventNotFound(self):
    	pass

    def testEventListSuccess(self):
    	pass

    @unittest.mock.patch('app.services.frontdesk.get_event_eligibility')
    def testEventAvailabilitySuccess(self, get_event_eligibility):
    	app.models.user.User.create({
            'id': 12,
            'name': 'John Staff', 
            'email': 'johnstaff@example.com', 
            'firstName': 'John', 
            'lastName': 'Staff', 
            'address': '439 Guerrero Street, CA 94110 US', 
            'birthdate': '2015-06-22', 
            'frontdeskId': 1, 
            'frontdeskToken': 'abc123'
        })
    	
    	get_event_eligibility.return_value = {
	        "person_id": 1,
	        "can_enroll": False,
	        "restrictions": [
	        {
	            "code": "full",
	            "description": "This event is full"
	        },
	        {
	            "code": "plan_required",
	            "description": "No available visits"
	        }]
	    }

    	response = self.app.get('/users/12/events/7/eligibility')
    	assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()