# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

#printing the number of quakes

total=0;
for quake in data["features"]:
    if(quake["properties"]["type"] is not None):
        total=total+1;

print("The total number of quakes are " + str(total));

#printing the number of quakes felt by more than 100 people
counter=0;

for quake in data["features"]:
    if(quake["properties"]["felt"]is not None and quake["properties"]["felt"]>=100):
        counter=counter+1;
print("The total number is " + str(counter));

#printing the most felt quake's properties

def getFelt(dataitem):
    mag = dataitem["properties"]["felt"]
    if mag is not None:
        return mag
    return 0

maxVal = max(data["features"],key=getFelt)
# print()

#printing the top 10 significant values
def sortVal(dataitem):
    value = dataitem["properties"]["sig"]
    if value is not None:
        return value
    return 0
sortedList = sorted(data["features"],key=sortVal,reverse=True)

for i in range(10):
    print("place is "+sortedList[i]["properties"]["place"] + "sig val is " + str(sortedList[i]["properties"]["sig"]))