import app

class User(app.db.Document):
	name = app.db.StringField(required=True)
	email = app.db.EmailField(required=True)
	frontdesk_id = app.db.IntField(required=True)
	access_token = app.db.StringField(required=True)
	first_name = app.db.StringField()
	middle_name = app.db.StringField()
	last_name = app.db.StringField()
	address = app.db.StringField()
	secondary_info_field = app.db.StringField()
	birthdate = app.db.DateTimeField()

	def serialize(self):
		return self.to_json()


#def create(**kwargs):
#	return User(kwargs)
