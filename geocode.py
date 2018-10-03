import requests
import googlemaps
import yaml

GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

gmaps_api = yaml.load(open('gmaps_api.yaml'))

params = {}

def getLoc(address):
	params["address"] = address
	params["key"] = gmaps_api['key']

	# Do the request and get the response data
	req = requests.get(GOOGLE_MAPS_API_URL, params=params)
	res = req.json()

	# Use the first result
	result = res['results'][0]

	geodata = dict()
	geodata['lat'] = result['geometry']['location']['lat']
	geodata['lng'] = result['geometry']['location']['lng']
	geodata['address'] = result['formatted_address']
	
	print([geodata['lat'], geodata['lng']])
	return ([geodata['lat'], geodata['lng']])

#print(geodata['lat']) // latitude
#print(geodata['lng']) // longitude

#print('{address}. (lat, lng) = ({lat}, {lng})'.format(**geodata))
