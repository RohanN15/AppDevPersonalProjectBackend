import googlemaps
import datetime
import json

API_KEY = 'AIzaSyBK4jB7zPp-GInC4pKMrTmfrllNDWNkLkA'

gmaps = googlemaps.Client(key=API_KEY)

start = '4213 Valley Dr, College Park, MD, 20742'
end = '19 Dickens Dr'
def getRoute(start, end):
    directions = gmaps.directions(start, end, mode='transit', departure_time=datetime.datetime.now())
    durations = []
    def find_durations(data):
        if isinstance(data, dict):
            if "duration" in data:
                durations.append(data["duration"])
            for value in data.values():
                find_durations(value)
        elif isinstance(data, list):
            for item in data:
                find_durations(item)
                
    find_durations(directions)
    print(durations[0]["text"])
getRoute(start, end)