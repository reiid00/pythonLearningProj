#Dictionary: Key-Value pairs, Unordered, Mutable

mydict={"name":"Max","age":28,"city":"New York"} # create dictionary

mydict2=dict(name="Mary",age=27,city="New York") # another way~

mydict["name"] # returns the value of key name

mydict["email"] = "max@tuts.com" # add new key-value pair to dictionary

mydict["email"] = "max12@tuts.com" # if the key exists, it overwrites the value

del mydict["email"] # delete key-value, this case email

mydict.pop("age") # another way to delete key-value

mydict.popitem() # removes last key-value

mydict["age"]=28

mydict["city"]="New York"

if "name" in mydict: # verify if it exists the key
    pass

try: # another way to verify if it exists
    mydict["name"]
except:
    pass

for key in mydict:
    pass

for key in mydict.keys():
    pass

for value in mydict.values():
    pass

for key, value in mydict.items():
    pass

mydict_cp = mydict # works as list, if we change mydict_cp it changes mydict

mydict_cpy = mydict.copy() # copies correctly

mydict_cpy = dict(mydict) # another way to copy

mydict={"name":"Max","age":28,"email":"max12@tuts.com"}

mydict2=dict(name="Mary",age=27,city="New York") 

mydict.update(mydict2) # overwrites the same keys, adds the new ones

my_tuple=1,2
mydict[my_tuple]=4 # possible to create keys with tuples, not with lists

print(mydict)
