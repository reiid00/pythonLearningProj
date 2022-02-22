# Sets: unordered, mutable, no duplicates

myset={1,2,3,1,2} # set is {1,2,3}

myset=set([1,2,3])

myset=set("Hello") # creates set with only on l, can be used to verify how many different chars a word has

myset=set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)

myset.remove(4) # removes elem, if doesnt exist raises exception

myset.discard(5) # removes elem, if doesnt exist nothing happens

myset.pop() # returns 1st value of myset and also removes it

# iterates same way as lists, for in loop
# if statement is the same as lists

odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens) # union of odds with evens

i=odds.intersection(primes) # intersection of odds with primes, only has the values that are in both sets

d=odds.difference(primes) # difference between odds and primes, returns values that are in the 1st set but not in the 2nd set

diff=odds.symmetric_difference(primes) # returns all the elements from the setA and setB but not the elems that are in the both sets, symmetric of difference

odds.update(primes) # adds the new values from set2 to set1

odds.intersection_update(evens) # updates the set by keeping only the elements found in both sets

odds.difference_update(primes) # updates the set by removing the elements found in the other set

odds.symmetric_difference_update(evens) #updates the set by only keeping the elements found in setA and setB but not elems found in both, symmetric of difference update

setA= {1,2,3,4,5,6}
setB={1,2,3}
setC={7,8}

setA.issubset(setB) # False, subset means all elems from the 1st set are in 2nd set

setB.issubset(setA) # True, all elems from setB are in setA

setB.issuperset(setA) # False, superset returns true if 1st set contains all elems from 2nd set

setA.issuperset(setB) # True, contains all elems from setB

setA.isdisjoint(setB) # False, returns true if setA and setB dont have any elem in common

setA.isdisjoint(setC) # True

#copying is the same as lists
