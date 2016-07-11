import app.utils.string
import importlib

class Base(object):
	def serialize(self):
		class_name = self.__class__.__name__
		module_name = app.utils.string.underscore(class_name)
		try:
			serializer_module = importlib.import_module('app.serializers.{}'.format(module_name))
		except ImportError:
			class_name = 'Base'
			serializer_module = importlib.import_module('app.serializers.base')
		serializer_class = getattr(serializer_module, class_name)
		serializer_instance = serializer_class(self)
		return serializer_instance.serialize()

	@classmethod
	def serialize_list(cls, models):
		class_name = cls.__name__
		module_name = app.utils.string.underscore(class_name)
		try:
			serializer_module = importlib.import_module('app.serializers.{}'.format(module_name))
		except ImportError:
			class_name = 'Base'
			serializer_module = importlib.import_module('app.serializers.base')
		serializer_class = getattr(serializer_module, class_name)
		return getattr(serializer_class, 'serialize_list')(models)