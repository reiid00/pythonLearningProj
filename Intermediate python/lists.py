#Lists : ordered, mutable, allows duplicate elements

myList = ["banana","coccun","cherry"] # create new list

myList2=list() # create empty list

myList2= [5,True,"apple","apple"] # create list with various types

item = myList[0] # item is banana

item=myList[1] # item is coccun

item=myList[-1] # item is cherry -2 would be coccun


if "banana" in myList: # check if banana is myList
    pass

len(myList) # prints the length of myList

myList.append("lemon") # appends lemon to the final of the list

myList.insert(1,"pear") # inserts pear at index 1

item = myList.pop() # item is lemon in this case(pops the last item in the list)

item = myList.remove("banana") # removes the 1st enccounter with that value

myList2.clear() # clears list

myList.reverse() # reverses list

myList.sort() # sorts list

listToSort=[4,3,1,0,9,10]

new_list = sorted(listToSort) # new_list will be sorted, listToSort wont

myList = [0] * 5 # creates list with 5 Zeros

myList2 = [1,3,5,2,3]

myList3=myList+myList2 # adds lists

a=myList3[1:5] # list from index 1 to index 5-1

a=myList3[:5] # list from beggining to index 5-1

a=myList3[5:] # list from index 5 to end

a=myList[::2] # Takes every 2nd item

a=myList[::-1] # Reverse list

list_org=["banana","cherry","apple"]

list_bad_cpy = list_org # with this assignment, every single thing you do to list_cpy it also does to list_org(both lists refere to the same list in the memory)

list_cpy=list_org.copy() # actual copy

list_cpy=list(list_org) # another way to actual copy

list_cpy=list_org[:] # another way(through slicing)

list_cpy.append("lemmon")

a=[1,2,3,4,5,6,7]
b=[i**2 for i in a] #syntax: expression for in loop in the list (in this case it gives us squared values)



