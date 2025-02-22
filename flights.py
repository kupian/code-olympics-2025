import os
import requests

flight_number = input("Flight number: ")

params = {
  'access_key': os.environ.get("FLIGHT_API", None),
  'flight_icao': flight_number
}

api_result = requests.get('https://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()
if len(api_response['data']) == 0:
    print("Flight not found")

for flight in api_response['data']:
    if flight.get("live", None) is not None:
        if flight['live']['is_ground'] is False:
            lat = flight['live']['latitude']
            long = flight['live']['longitude']
            dep = flight['departure']['airport']
            arr = flight['arrival']['airport']
            est = flight['arrival']['estimated']
            print(f"Flight {flight_number} is currently at position: {lat}, {long}. En route from {dep} to {arr} with est. arrival time: {est}")
        else:
            print("No live data available")