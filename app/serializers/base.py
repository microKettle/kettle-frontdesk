import json
import app.utils.string

class Base(object):
    def __init__(self, model):
        self.model = model
        self.attributes = None
        self.payload_key = None
    
    def _payload_key(self):
        if self.payload_key != None:
          return payload_key
        return app.utils.string.camelize(self.model.__class__.__name__)

    def _attributes(self):
        if self.attributes != None:
            return self.attributes

        result = []
        for attribute in self.model.__dict__.keys():
            if attribute.startswith('__'):
                break
            if callable(getattr(self.model, attribute)):
                break
            result.append(attribute)
        return result

    def hash(self):
        result = {}
        for attribute in self._attributes():
            result[app.utils.string.camelize(attribute)] = getattr(self.model, attribute)
        return result

    def serialize(self):
        result = self.hash()
        if self._payload_key() != False:
            result = {
                self._payload_key(): result
            }
        return json.dumps(result)

    @classmethod
    def serialize_list(cls, models):
        result = []
        payload_key = None
        for model in models:
            serializer = Base(model)
            result.append(serializer.hash())
            if payload_key == None:
                payload_key = serializer._payload_key()
        if payload_key != False:
            result = {
                app.utils.string.pluralize(payload_key): result
            }
        return json.dumps(result)


