import app.models.base

class Event(app.models.base.Base):
	def __init__(self, id, name, description, startAt, endAt, timezone, state, full, capacityRemaining):
		self.id = id
		self.name = name
		self.description = description
		self.startAt = startAt
		self.endAt = endAt
		self.timezone = timezone
		self.state = state
		self.full = full
		self.capacityRemaining = capacityRemaining

	@staticmethod
	def create(attributes):
		del(attributes['url'])
		del(attributes['service_id'])
		del(attributes['location_id'])
		del(attributes['event_id'])
		del(attributes['staff_members'])
		attributes['startAt'] = attributes.pop('start_at', None)
		attributes['endAt'] = attributes.pop('end_at', None)
		attributes['capacityRemaining'] = attributes.pop('capacity_remaining', None)
		return Event(**attributes)