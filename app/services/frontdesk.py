import app
import json
import urllib3

def get_access_token(temporary_token):
	http = urllib3.PoolManager()
	response = http.request('POST', app.instance.config['FRONTDESK_SETTINGS']['URL_AUTH'] + '/token?grant_type=authorization_code' + '&code=' + temporary_token + '&redirect_uri=' + app.instance.config['FRONTDESK_SETTINGS']['REDIRECT_URL'] + '&client_id=' + app.instance.config['FRONTDESK_SETTINGS']['CLIENT_ID'] + '&client_secret=' + app.instance.config['FRONTDESK_SETTINGS']['CLIENT_SECRET'])
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		return parsed_data['access_token']
	return response.data

def get_user_info(access_token):
	http = urllib3.PoolManager()
	headers = {'Authorization': 'Bearer ' + access_token}
	response = http.request('GET', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + '/front/people/me', headers=headers)
	if (response.status == 200):
		parsed_data = json.loads(response.data.decode('utf-8'))
		user_data = parsed_data['people'][0]
		return user_data
	return False 