import re

def camelize(value):
	pattern = re.compile('\w+')
	result = ''

	for word in pattern.findall(value):
		if result == '':
			result += word[0].lower() + word[1:]
			continue
		result += word[0].uppercase() + word[1:]
	return result

def capitalize(value):
	return value[0].uppercase() + value[1:]

def underscore(value):
	pattern = re.compile('\w+')
	result = ''

	for word in pattern.findall(value):
		for letter in word:
			if result != '' and letter == letter.upper():
				result += '_'
			result += letter.lower()
	return result

def pluralize(value):
	result = '{0}s'.format(value)
	return result