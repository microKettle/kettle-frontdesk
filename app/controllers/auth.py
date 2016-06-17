import app.models
import flask

module = flask.Blueprint('auth', __name__, url_prefix='/auth')

@module.route('/test', methods=['GET'])
def test():
	return 'Test'

@module.route('/sign_in', methods=['POST'])
def sign_in():
	return 'Sign In'

@module.route('/sign_out', methods=['POST'])
def sign_out():
	return 'Sign Out'