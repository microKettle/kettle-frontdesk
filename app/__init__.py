import flask
import flask_mongoengine

db = flask_mongoengine.MongoEngine()

instance = flask.Flask(__name__)
instance.config.from_object('config')
db.init_app(instance)

import app.controllers.auth
instance.register_blueprint(app.controllers.auth.module)