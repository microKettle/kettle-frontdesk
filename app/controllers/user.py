import app.models.user
import app.services.frontdesk
import app.services.session
import flask
import bson.objectid
import json

module = flask.Blueprint('users', __name__, url_prefix='/users')

@module.route('/<int:id>', methods=['GET'])
def read(id):
	try:
		user = app.models.user.User.get_by_id(id)
	except app.models.user.User.DoesNotExist:
		return ('', 404)
	return (user.serialize(), 200)

@module.route('', methods=['POST'])
def create():
	try :
		payload = json.loads(flask.request.get_data().decode('utf-8'))
	except ValueError:
		return ('', 422)

	if ('user' not in payload):
		return ('', 422)

	if ('temporaryToken' not in payload['user']):
		return ('', 422)

	access_token = app.services.frontdesk.get_access_token(payload['user']['temporaryToken'])
	if not access_token:
		return ('', 400)
	
	user_data = app.services.frontdesk.get_user_info(access_token)
	if not user_data:
		return ('', 400)
	user_data['frontdeskToken'] = access_token

	try:
		user = app.models.user.User.find_by('frontdeskId', user_data['frontdeskId'])
		user.update(user_data)
	except app.models.user.User.DoesNotExist:
		user = app.models.user.User.create(user_data)

	return (user.serialize(), 201)

