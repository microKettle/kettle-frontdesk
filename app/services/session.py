import app
import uuid

def create(user):
	session_token = str(uuid.uuid1())
	app.redis.set(session_token, user.id)
	return session_token

def delete(session_token):
	app.redis.delete(session_token)

def exists(session_token):
	return app.redis.get(session_token) != None