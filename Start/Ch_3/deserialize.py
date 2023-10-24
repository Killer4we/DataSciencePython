# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("filteredQuake.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # print(row)
        result.append(
            {
                "place":row[0],
                "magnitude":row[1],
                "link":row[2],
                "place":row[3]
            }
        )

pprint.pp(result)
