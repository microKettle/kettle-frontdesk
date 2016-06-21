import flask
import flask.ext.redis
import flask_mongoengine
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')

db = flask_mongoengine.MongoEngine()
redis = flask.ext.redis.FlaskRedis()

instance = flask.Flask(__name__)
instance.config.from_object('config')

db.init_app(instance)
redis.init_app(instance)

import app.controllers.auth
instance.register_blueprint(app.controllers.auth.module)