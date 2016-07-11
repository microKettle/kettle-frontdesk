import app
import json
import urllib3

def get_access_token(temporary_token):
	http = urllib3.PoolManager()
	response = http.request('POST', app.instance.config['FRONTDESK_SETTINGS']['URL_AUTH'] + '/token?grant_type=authorization_code' + '&code=' + temporary_token + '&redirect_uri=' + app.instance.config['FRONTDESK_SETTINGS']['REDIRECT_URL'] + '&client_id=' + app.instance.config['FRONTDESK_SETTINGS']['CLIENT_ID'] + '&client_secret=' + app.instance.config['FRONTDESK_SETTINGS']['CLIENT_SECRET'])
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		return parsed_data['access_token']
	return False

def get_user_info(access_token):
	http = urllib3.PoolManager()
	headers = {'Authorization': 'Bearer ' + access_token}
	response = http.request('GET', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + '/front/people/me', headers=headers)
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		user_data = parsed_data['people'][0]
		return {
			'name': user_data['name'],
			'email': user_data['email'],
			'firstName': user_data['first_name'],
			'middleName': user_data['middle_name'],
			'lastName': user_data['last_name'],
			'address': user_data['address'],
			'birthdate': user_data['birthdate'],
			'frontdeskId': user_data['id']
		}
	return False

def get_event_info(event_id, access_token):
	http = urllib3.PoolManager()
	headers = {'Authorization': 'Bearer ' + access_token}
	response = http.request('GET', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + '/front/event_occurrences/{}'.format(event_id), headers=headers)
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		event_data = parsed_data['event_occurences'][0]
		return event_data
	return False

def get_event_list(access_token):
	http = urllib3.PoolManager()
	headers = {'Authorization': 'Bearer ' + access_token}
	response = http.request('GET', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + '/front/event_occurrences', headers=headers)
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		events_data = parsed_data['event_occurences']
		return events_data
	return False

def get_event_eligibility(event_id, access_token):
	http = urllib3.PoolManager()
	headers = {'Authorization': 'Bearer ' + access_token}
	response = http.request('GET', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + '/front/event_occurrence/{}/enrollment_eligibilities'.format(event_id), headers=headers)
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		eligibility_data = parsed_data['enrollment_eligibilities'][0]
		return eligibility_data
	return False