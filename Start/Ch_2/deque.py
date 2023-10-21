# deque objects are like double-ended queues

# import collections
from collections import deque
import string


# TODO: initialize a deque with lowercase letters

d = deque(string.ascii_lowercase);

# TODO: deques support the len() function
# print(d.count());.
# print(d.maxlen());
print(len(d));
# TODO: deques can be iterated over
for ele in d:
    print(ele.upper());
# TODO: manipulate items from either end
d.pop();
d.popleft();
d.appendleft('a');
d.append('z');
# TODO: use an index to get a particular item
print(d[1]);