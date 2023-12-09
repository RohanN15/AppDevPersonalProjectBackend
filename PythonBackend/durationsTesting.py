import json
import re
f = open("test.txt")
json_data = json.load(f)

durations = []
minutes = []

def find_durations(data):
    if isinstance(data, dict):
        if "duration" in data:
            durations.append(data["duration"])
        for value in data.values():
            find_durations(value)
    elif isinstance(data, list):
        for item in data:
            find_durations(item)
            
find_durations(json_data)

print(durations[0]["text"])

all_instructions = []

def find_instructions(data):
    if isinstance(data, dict):  
        if "html_instructions" in data:
            all_instructions.append(data["html_instructions"])
        for value in data.values():
            find_instructions(value)
            
    elif isinstance(data, list):
         for item in data:
             find_instructions(item)

find_instructions(json_data)
f = open("directions.txt", 'w')
f.write(' '.join(all_instructions))
f.close()

