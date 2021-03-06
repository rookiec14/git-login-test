import os
# The values below are here as an example - please insert your own.


#generate your own unique cookie key here to secure your session cookie
#Tip: In a python interpreter you can use "os.urandom(64).encode('base64')" to generate the key
COOKIE_KEY = '4PqH814L0QidXlfRK/BX5moRTdxzbUbNMN64cGfXTtrQtoJCi010fuV3te4Swk/YLKNaRBtXqE9G\n8joKosECZw==\n'

# URL for the development app engine server
_DEV_SERVER_URL = 'http://localhost:9080'

# URL for the production app engine server
_PROD_SERVER_URL = 'http://git-login-test.appspot.com'

# Your API_KEY for identity toolkit on the Google dev console
API_KEY = 'AIzaSyByvhjnpzR229OAjLmOLVULsuMoDXVNOJ0'

# Debug mode
_DEBUG = True


if os.environ['SERVER_SOFTWARE'].startswith('Development'):
    SERVER_URL = _DEV_SERVER_URL
else:
    SERVER_URL = _PROD_SERVER_URL
