import app
import json

class User(app.db.Document):
	resource_id = app.db.SequenceField(collection_name="user.counter")
	name = app.db.StringField(required=True)
	email = app.db.EmailField(required=True)
	firstName = app.db.StringField()
	middleName = app.db.StringField()
	lastName = app.db.StringField()
	address = app.db.StringField()
	birthdate = app.db.StringField()
	frontdeskId = app.db.IntField(required=True)
	frontdeskToken = app.db.StringField()

	def update(self, attributes):
		for (key, value) in attributes.items():
			self.__setattr__(key, value)
		self.save()

	def serialize(self):
		user = json.loads(self.to_json())
		user['id'] = user['resource_id']
		del(user['resource_id'])

		return json.dumps({
          'user': user
		})

	@staticmethod
	def create(attributes):
		user = User(**attributes)
		user.save()
		return User.get_by_id(user.resource_id)

	@staticmethod
	def get_by_id(id):
		return User.objects.get(resource_id=id)

	@staticmethod
	def find_by(key, value):
		return User.objects.get(**params = {
			key: value
		})
