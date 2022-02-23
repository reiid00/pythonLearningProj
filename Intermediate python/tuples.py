import sys
import timeit

# Tuple: ordered, immutable, allows duplicate elements
# Difference bewteen list and tuple: tuples cannot be changed after creation

myTuple="Max",28,"Boston" # create a Tuple

myTuple9=("Max",) # creates a tuple with 1 element

myTuple=tuple(["Max",28,"Boston"]) #create tuple from list

myList = ["Max",28,"Boston"]

myTuple = tuple(myList)

item = myTuple[0] # gives the 1st item --> Max , works as a list

# myTuple[0] = "Tim" # this does not work --> TypeError: 'tuple' object does not support item assignment

for i in myTuple: # iterate tuple
    i=i

if "Max" in myTuple: # verify if Max is in the tuple
    pass

my_tuple = 'a','b','p','c','k','e','p'

len(my_tuple) # length my_tuple

my_tuple.count('p') # count how many times p is in tuple

my_tuple.index('p') # returns first occurance of letter p

my_list = list(my_tuple) # list from the tuple

my_tuple2 = tuple(my_list) # converst back to tuple

a=1,2,3,5,2,3,5,7,9,10,12,14,16,16,23,25,3

b=a[1:4] # tuple from index 1 to index 4-1, works the same as list

myTuple = "Vasco",21,"Porto"

name,age,city=myTuple # num of elements needs to be the same as the tuple
#name is Vasco
#age is 21
#city is Porto

my_tuple = 0,1,2,3,4

i1,*i2,i3 = my_tuple
#i1 is 1st element
#i3 is last element
#i2 is a list with all the elements between the 1st and the lasts

my_list=[0,1,2,3,4,5,"Vasco","Porto","hello",True]
my_tuple=0,1,2,3,4,5,"Vasco","Porto","hello",True
sys.getsizeof(my_list) # 152 bytes
sys.getsizeof(my_tuple) # 120 bytes
#list is larger even though it has the same elements
timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000) # 0.043099100003018975
timeit.timeit(stmt="0,1,2,3,4,5",number=1000000) # 0.008761100005358458
