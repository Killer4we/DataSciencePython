# Demonstrate the usage of namdtuple objects

from collections import namedtuple


# TODO: create a Point namedtuple
# X-coordintate=0
Point = namedtuple("Point","Xcoordinate Ycoordinate");

P1 = Point(12,13);
P2 = Point(23,34)
print(P1,P2); 
P1 = P1._replace(Xcoordinate = 200);
print(P1);

# TODO: use _replace to create a new instance
