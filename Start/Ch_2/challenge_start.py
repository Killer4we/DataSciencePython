# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict

# open the data file and load the JSON
with open("DataSciencePython\Start\Ch_2\\30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


quakescounter = defaultdict(int)

for event in data['features']:
    quakescounter[event['properties']['type']] +=1

print(quakescounter)