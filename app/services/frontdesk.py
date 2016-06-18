import urllib3
import app

def get_access_token(temporary_token):
	http = urllib3.PoolManager()
	response = http.request('POST', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + '/oauth/token?grant_type=authorization_code' + 'code=' + temporary_token + '&redirect_uri=' + app.instance.config['FRONTDESK_SETTINGS']['REDIRECT_URL'] + '&client_id=' + app.instance.config['FRONTDESK_SETTINGS']['CLIENT_ID'] + '&client_secret' + app.instance.config['FRONTDESK_SETTINGS']['CLIENT_SECRET'])
	if (response.status == 200):
		parsed_data = json.loads(response.data)
		return parsed_data['access_token']
	return False

def get_user_info(access_token):
	http = urllib3.PoolManager()
	headers = urllib3.util.make_headers(Authorization='Bearer: ' + access_token)
	response = http.request('GET', app.instance.config['FRONTDESK_SETTINGS']['URL_API'] + 'front/people/me', headers=headers)
	if (response.status == 200):
		parsed_data = json.loads(response.data)
		user_data = parsed_data['people'][0]
		user_data['frontdesk_id'] = user_data['id']
		return user_data
	return False 