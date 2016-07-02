import app.models.user
import app.services.frontdesk
import flask
import json

module = flask.Blueprint('events', __name__, url_prefix='/users/<int:user_id>/events')

@module.route('/<int:id>', methods=['GET'])
def read(user_id, id):
	try:
		user = app.models.user.User.get_by_id(user_id)
	except app.models.user.User.DoesNotExist:
		return ('', 404)

	event_data = app.services.frontdesk.get_event_info(id, user.frontdeskToken)
	if event_data == False:
		return ('', 404)

	result = {
		'event': event_data
	}
	return (json.dumps(result), 200)

@module.route('/<int:id>/eligibility', methods=['GET'])
def read_eligibility(user_id, id):
	try:
		user = app.models.user.User.get_by_id(user_id)
	except app.models.user.User.DoesNotExist:
		return ('', 404)

	eligibility_data = app.services.frontdesk.get_event_eligibility(id, user.frontdeskToken)
	if eligibility_data == False:
		return ('', 404)

	result = {
		'eligibility': eligibility_data
	}
	return (json.dumps(result), 200)