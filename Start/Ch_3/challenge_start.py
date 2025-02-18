# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv


# open the data file and load the JSON
with open("DataSciencePython\\30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def getSig(dataitem):
    if dataitem["properties"]["sig"] is not None:
        return dataitem["properties"]["sig"]
    return 0

significant = sorted(data["features"],key=getSig,reverse=True)
for i in range(40):
    print(significant[i]["properties"]["place"],str(significant[i]["properties"]["sig"]))
# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

header = ["Magnitude","Place","felt","date","map link"]

rows = []

with open("challenge3.csv","w") as csvfile:
    writer = csv.writer(csvfile,delimiter=' ')
    writer.writerow(header) #Writing header
