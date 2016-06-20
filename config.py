import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
MONGODB_SETTINGS = {
	'db': os.environ.get('MONGODB_DB'),
	'host': os.environ.get('MONGODB_HOST', 'localhost')
}

FRONTDESK_SETTINGS = {
	'URL_AUTH': 'https://lutece.frontdeskhq.com/oauth',
	'URL_API': 'https://lutece.frontdeskhq.com/api/v2',
	'CLIENT_ID': 'nMaOVbUKTKfYJXZva8ix2bpbRtDJMUIzT9BEwZXs',
	'CLIENT_SECRET': 'p631IGbxHS8Phbcpo0LYyTRemNGrTlHSHx2pIU4C',
	'REDIRECT_URL': 'http://kettle-1.kettle.50023ace.cont.dockerapp.io'
}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"