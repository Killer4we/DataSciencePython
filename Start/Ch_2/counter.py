# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

# TODO: Create a Counter for class1 and class2

c1= Counter(class1);
c2 = Counter(class2);
# TODO: How many students in class 1 named James?
print(c1["James"]);
print(c2["James"]);
# TODO: How many students are in class 1?
print("The total number of students in class1 are " + str(sum(c1.values())));
# TODO: Combine the two classes

c1.update(c2);
print("The total number of students in class 1 after adding c2 are " + str(sum(c1.values())));
# print(c1);
# TODO: What's the most common name in the two classes?
print(c1.most_common());
# TODO: Separate the classes again
c1.subtract(c2);
# TODO: What's common between the two classes?
print(c1&c2);