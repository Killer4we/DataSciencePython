# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value

# min_value = min(values)
# min_string = min(strings)
# print("The minimum value among the values list is " + str(min_value))
# print("The minimum value among the strings list is " + str(min_string))

# TODO: The max() function finds the maximum value

# max_value = max(values)
# max_string = max(strings)
# print("The maximum value among the values list is " + str(max_value))
# print("The maximum value among the strings list is " + str(max_string))

# TODO: define a custom "key" function to extract a data field

# print("The minimum string now after using the key function is " + min(strings,key=len))
# print("The maximum string now after using the key function is " + max(strings,key=len))

# TODO: open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
# print(data["features"]["mag"])
print(data["metadata"]["title"])
print(len(data["features"]))

def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if(magnitude is None):
        magnitude = 0
    # else:
    #     return float(magnitude)
    return float(magnitude)

print(min(data["features"],key=getmag))
print(max(data["features"],key=getmag))