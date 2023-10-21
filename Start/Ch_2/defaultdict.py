# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ["apple", "pear", "orange", "banana",
          "apple", "grape", "banana", "banana"]

# TODO: use a dictionary to count each element
fruitCounter1 = defaultdict(int)
fruitCounter2 = defaultdict(lambda: 50)

# TODO: Count the elements in the list
for fruit in fruits:
    fruitCounter1[fruit]+=1

for fruit in fruits:
    fruitCounter2[fruit]+=1


# TODO: print the result
print(fruitCounter1)
print(fruitCounter2)
# # for value in fruitCount.