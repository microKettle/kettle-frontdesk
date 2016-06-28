import flask
import flask_mongoengine
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

db = flask_mongoengine.MongoEngine()

instance = flask.Flask(__name__)
instance.config.from_object('config')

db.init_app(instance)

import app.controllers.user
instance.register_blueprint(app.controllers.user.module)