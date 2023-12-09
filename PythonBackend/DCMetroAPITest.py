import requests
import os
import json

# api_key = os.getenv("e13626d03d8e4c03ac07f95541b3091b") 

url = "https://api.wmata.com/Rail.svc/json/jSrcStationToDestStationInfo"

origin = "B06" # Gallery Pl code 
destination = "A01" # Metro Center code

def get_eta(origin, destination):

    params = {
        "FromStationCode": origin,
        "ToStationCode": destination,
        "api_key": "e13626d03d8e4c03ac07f95541b3091b"
  
    }

    response = requests.get(url, params=params)
    data = json.loads(response.text)
    # eta = data['RailTimeInformation']['DestinationStationElapsedTime']

    # print(f"Estimated travel time between {origin} and {destination} is {eta} minutes")
    print(data)
    
get_eta(origin, destination)