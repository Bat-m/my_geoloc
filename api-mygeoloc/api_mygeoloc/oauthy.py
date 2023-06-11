from authlib.integrations.flask_client import OAuth
from flask import current_app
import os
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'


oauthI = OAuth(current_app)
oauthI.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_id = os.getenv('GOOGLE_CLIENT_ID'),
    client_secret = os.getenv('GOOGLE_CLIENT_SECRET'),
    client_kwargs={
        'scope': 'openid email profile'
    },
    
)

