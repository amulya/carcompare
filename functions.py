from flask import Flask
import geocode # do i even need this?

# user auth
from user_rides.auth import AuthorizationCodeGrant

from user_rides.session import Session
from user_rides.client import UberRidesClient

import yaml

"""
# in routes.py: make form for these
start_addr = # user input
end_addr = # user input
"""

# Returns latitude + longitude (floats) of an address
def getCoords(address):
	start_loc = geocode.getLoc(address)
	lat = start_loc[0]
	lng = start_loc[1]
	return [lat, lng]


# Returns list of available products @ current loc 
def getProducts(address): 
	loc = getCoords(address)
	start_lat = loc[0]
	start_lng = loc[1]
	product_response = client.get_products(start_lat, start_lng)
	products = product_response.json.get('products')
	return products

# Get price estimates
def getPrices(address1, address2):
	#variables
                # start_lat
                # start_lng
                # end_lat
                # end_lng
                # seat_count - for uberPOOL (optional)
	
	# address 1 coords
	loc1 = getCoords(address1)
	start_lat = loc1[0]
	start_lng = loc11]

	# address 2 coords
	loc2 = getCoords(address2)
	end_lat = loc2[0]
	end_lng = loc2[1]
	
	# get seat count through form????
		# seat_count = FORMRESPONSEE!!!
		# else seat_count = None

	price_response = None

	if seat_count:
		price_response = client.get_price_estimates(start_lat, start_lng, end_lat, end_lng, seat_count)
	else:
		price_response = client.get_price_estimates(start_lat, start_lng, end_lat, end_lng)
	
	price_estimate = price_response.json.get('prices')
	return price_estimate

# Get time estimates
def getTimes(address1, address2):
	#variables
                # start/end latitude
                # start/end longitude
                # product_id (optional)
	
	# address 1 coords
	loc1 = getCoords(address1)
	start_lat = loc1[0]
	start_lng = loc1[1]

	# address 2 coords
        loc2 = getCoords(address2)
        end_lat = loc2[0]
        end_lng = loc2[1]

	# get product_id thru form response?
		# product_id = FORMRESPONSEEEEE
		# use a method to get actual id?
		# else product_id = None
	
	time_response = None
	
	if product_id:
		time_response = client.get_time_estimates(start_lat, start_lng, end_lat, end_lng, product_id)
	else:
		time_response = client.get_time_estimates(start_lat, start_lng, end_lat, end_lng)
	time_estimate = time_response.json.get('times')
	return time_estimate
