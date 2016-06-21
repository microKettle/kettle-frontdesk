import app.models.user
import app.services.frontdesk
import app.services.session
import flask
import bson.objectid
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
	access_token = app.services.frontdesk.get_access_token(temporary_token)
	if not access_token:
		return ('', 401)
	
	user_data = app.services.frontdesk.get_user_info(access_token)
	if not user_data:
		return ('', 401)

	try:
		user = app.models.user.User.objects.get(frontdesk_id=user_data['id'])
	except app.models.user.User.DoesNotExist:
		user = app.models.user.User(frontdesk_id=user_data['id'])

	user.name = user_data['name']
	user.email = user_data['email']
	user.access_token = access_token
	user.save()

	result_data = {
		'user_id': str(user.id),
		'session_token': app.services.session.create(user)
	}
	
	return (json.dumps(result_data), 200)
