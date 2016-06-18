import app.models.user
import app.services.frontdesk
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
	access_token = app.services.frontdesk.get_access_token(temporary_token)
	if access_token:
		user_data = app.services.frontdesk.get_user_info(access_token)
		user = app.models.user.User(frontdesk_id=user_data['frontdesk_id'], name=user_data['name'], email=user_data['email'], access_token=access_token)
		user.save()
		return (user.serialize(), 204)
	return ('', 404)
