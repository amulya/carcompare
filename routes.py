from flask import Flask
import geocode #geocode.getLoc

# user auth
from user_rides.auth import AuthorizationCodeGrant

from user_rides.session import Session
from user_rides.client import UberRidesClient

import yaml

# Rider Authorization

auth_flow = AuthorizationCodeGrant( <CLIENT_ID>,
    <SCOPES>,
    <CLIENT_SECRET>,
    <REDIRECT_URI>)
        #variables
                # client ID
                # scopes
                # client_secret
                # redirect_URI
auth_url = auth_flow.get_authorization_url()




# Session using server token

session = Session(server_token=TOKEN!!!!!!!!!!!!!!!!!!!!!)
client = UberRidesClient(session)

# Session using user authorization

session = auth_flow.get_session(redirect_url)
client = UberRidesClient(session, sandbox_mode=True)
credentials = session.oath2credential
	# store in secure data store so riders dont need to go thru authorization process repeatedly

#Fetch user profile

response = client.get_user_profile()
profile = response.json

first_name = profile.get('first_name')
last_name = profile.get('last_name')
email = profile.get('email')


#Fetch a user's activity

response = client.get_user_activity()
history = response.json
