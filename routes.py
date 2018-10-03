from flask import Flask, url_for, render_template, request, redirect
import geocode #geocode.getLoc
import functions
import functions
#import uber_rides

app = Flask(__name__)

# user auth
from uber_rides.auth import AuthorizationCodeGrant

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

import yaml
uber_yaml = yaml.load(open('uber_api.yaml'))
client_id = uber_yaml['client_id']
client_secret = uber_yaml['client_secret']
server_token = uber_yaml['server_token']

# Session using server token
session = Session(server_token='nPtXNDxWWWHlZ8CUa6doAnyED_6LzfC9GF8rvSKM')
client = UberRidesClient(session)

# Rider Authorization + Session
	#variables
                # client ID
                # scopes: General or privileged
                # client_secret
                # redirect_URI
		# state token??

"""
auth_flow = AuthorizationCodeGrant(client_id,
    {'history', 'profile', 'all_trips', 'request', 'request_receipt'},
    client_secret,
    'http://localhost:8080/', None)

auth_url = auth_flow.get_authorization_url()
print('1')
redirect_url = "http://localhost:8080/?code=JA.VUNmGAAAAAAAEgASAAAABwAIAAwAAAAAAAAAEgAAAAAAAAG8AAAAFAAAAAAADgAQAAQAAAAIAAwAAAAOAAAAkAAAABwAAAAEAAAAEAAAAAxNkXdRPBfwzs8fTBP0EEBsAAAA-K3iTaxsDPnu7mb5DXEbzkALkRHYNRvq0XQc3mOlj2KQXmXSrFC0rrrVxZTwkv5j3p_D_4rg_wsQQAK_uqKTi8oXj8JeGpdRT170HAm2WRVOSkCwXkIjgQYOrTAU8S1vyR6ykSxCBgBRWHYtDAAAAJIgNWkl2zV1j9xelyQAAABiMGQ4NTgwMy0zOGEwLTQyYjMtODA2ZS03YTRjZjhlMTk2ZWU"
#print(redirect_url)

# Session
session = auth_flow.get_session(redirect_url)
"""


client = UberRidesClient(session, sandbox_mode=True)
#credentials = session.oath2credential
	# store in secure data store so riders dont need to go thru authorization process repeatedly

@app.route('/', methods=['GET', 'POST'])
def index():
	products = None
	price_estimate = None
	time_estimate = None
	if request.method == 'POST':
		formInfo = request.form
		start = formInfo['start']
		end = formInfo['end']
		
		# methods: getProducts, getPrices, getTimes
		# using address 1, can ID available services at curr location
		#products = getProducts(start)
		# using address 1 + 2, can get price/time estimates
		price_estimate = functions.getPrices(start, end, client) 
		#time_estimate = functions.getTimes(start, end, client)
		return render_template('index.html', products=None, price_estimate=price_estimate, time_estimate=None)
	# display info on home page for now
	return render_template('index.html', products=products, price_estimate=price_estimate, time_estimate=time_estimate)

# Fetch results
@app.route('/results', methods=['GET'])
def results():
	products=None
	time_estimate = None
	return render_template('results.html', products=products, price_estimate=price_estimate, time_estimate=time_estimate)

# Fetch user profile
@app.route('/profile', methods = ['GET'])
def profile():
	response = client.get_user_profile()
	profile = response.json

	first_name = profile.get('first_name')
	last_name = profile.get('last_name')
	email = profile.get('email')
	
	return render_template('profile.html', first_name=first_name, last_name=last_name, email=email)

#Fetch a user's activity
@app.route('/activity', methods=['GET'])
def activity():
	response = client.get_user_activity()
	history = response.json
	return render_template('activity.html')

if __name__ == '__main__':
        #app.config['SESSION_TYPE'] = 'filesystem'
        app.run(debug=True)
