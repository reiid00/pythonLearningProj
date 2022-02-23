# collections: Counts, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a="aaaabbccvvvvbbbbcccc"

my_counter=Counter(a) # dictionary with all the differenct chars as Keys and the count(times theyre in the string) as Values, in order of values

most_common=my_counter.most_common(1) # returns a list with tuples in it of X most common types

my_counter.most_common(2)[1][0]
# Syntax:
# Returns list as [(a:4),(b:4)]
# most_common(X)[Y][Z]
# X: num of tuples in descending order
# Y: num of tuple we want
# Z: 0 if we want the key, 1 if we want the Value

list(my_counter.elements())# returns iterable with all the elements, convert to list so it is understandeable, alphabetic order

Point=namedtuple("Point","x,y") # creates a class Point with the fields x and y

pt=Point(20,10)
# print(pt,pt.x,pt.y)

ordered_dict=OrderedDict()
ordered_dict["b"]=1
ordered_dict["c"]=2
ordered_dict["d"]=3
ordered_dict["e"]=4
ordered_dict["a"]=0

ordered_dict # OrderedDict([('b', 1), ('c', 2), ('d', 3), ('e', 4), ('a', 0)])

default_dict=defaultdict(int) # default type: (in this case) int

default_dict["a"]=1
default_dict["b"]=2
default_dict["c"]=3

default_dict # defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})

default_dict["a"] # 1

default_dict["d"] # 0, it returns the default value if the data type if the Key doesn't exist

d=deque()

d.append(1)
d.append(2)
d.appendleft(3)

d # deque([3, 1, 2])

d.pop()

d # deque([3, 1])

d.popleft()

d # deque([1])

d.clear() # clears

d.extend([4,5,6]) # appends to the right
d.extendleft([1,2,3]) # appends to the left, 1 by 1, so: 3,2,1

d # deque([3, 2, 1, 4, 5, 6])

d.rotate(1) # rotates all elems X times to the right

d # deque([6, 3, 2, 1, 4, 5])

d.rotate(-1) # rotates all elems X times to the left

d # deque([3, 2, 1, 4, 5, 6])






