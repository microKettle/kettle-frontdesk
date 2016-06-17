import app.controllers.auth
import flask

instance = flask.Flask(__name__)
instance.config.from_object('config')
instance.register_blueprint(app.controllers.auth.module)