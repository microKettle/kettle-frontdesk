import app.models.user
import flask
import json

module = flask.Blueprint('auth', __name__, url_prefix='/auth')

@module.route('/sign_in', methods=['POST'])
def sign_in():
	return 'Sign In'

@module.route('/sign_out', methods=['POST'])
def sign_out():
	return 'Sign Out'

@module.route('/callback', methods=['GET'])
def callback():
	temporary_token =  flask.request.args.get('code')
	#then play the token to the frontdesk server and get access token
	access_token = 'abc123'
	#then play the access_token to get the informations on the user
	data = {
		'id': 1,
		'name': 'Foo Bar',
		'email': 'foobar@mail.com',
		'access_token': access_token
	}
	user = app.models.user.User(frontdesk_id=data['id'], name=data['name'], email=data['email'], access_token=access_token)
	user.save()
	return json.dumps({'token': access_token})
