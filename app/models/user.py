from app import db

class User(db.Document):
	name = db.StringField(required=True)
	email = db.EmailField(required=True)
	frontdesk_id = db.IntField(required=True)
	access_token = db.StringField(required=True)
	first_name = db.StringField()
	middle_name = db.StringField()
	last_name = db.StringField()
	address = db.StringField()
	secondary_info_field = db.StringField()
	birthdate = db.DateTimeField(),


#def create(**kwargs):
#	return User(kwargs)
