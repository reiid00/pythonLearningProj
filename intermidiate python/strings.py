from timeit import default_timer as timer

# Strings: ordered, immutable, text representation

my_string = """Hello 
World""" # prints with a paragraph in between Hello and World

my_string = """Hello \
World"""  # prints everything in the same line~

char = my_string[0] # returns char at pos X, -X returns from the last

# my_string[0] = 'c' # does not work, strings are immutable

substring = my_string[1:5] # substring will have chars from X to Y-1, works the same way as the others

for i in my_string: # iterate for in loop for all the chars in string
    pass

if "i" in my_string: # verifies if X is in my string
    pass


my_string = "    Hello World     "
my_string = my_string.strip() # removes the wide spaces, does not change the string, to it needs to be assigned
                              # thats because the string is immutable

my_string.upper()

my_string.lower()

my_string.startswith("H")

my_string.endswith("d")

my_string.find('o') # returns the position it finds the 1st o

my_string.count('o')

my_string=my_string.replace("Hello","New") # replaces the word Hello with New, needs to be assigned
                                           # doesnt give an error if the 1st word doesnt exist, it simply doesnt replace

my_string = "hello,everyone,reading,this"
my_list=my_string.split(",") # splits by whatever we put inside the func
my_list.append("and")
my_list.append("beyond")
new_string=' '.join(my_list) # passes from list to string, the ' ' means that between each string in the list, it will add a space in this case, can be whatever we want

my_list=['a']*10000000

start = timer()
#BAD PYTHON CODE
my_string = ''
for i in my_list:
    my_string+=i

stop = timer()

print(f"Time for Bad Python was {stop-start}")

start = timer()
#GOOD PYTHON CODE
my_string=''.join(my_list)

stop = timer()

print(f"Time for Good Python was {stop-start}")

#OLD FORMATTING
var = "Tom"
my_string="the variable is %s" %var # %s is a placeholder which will be filled with the variable var with %var

# %s strings: "Tom"
# %d integer or decimal value : 32
# %f float values: 3.2131321, to specify how many digits %.2f(2 digits)

#SEMI-OLD FORMATTING
my_string="the variable is {}".format(var) # this works for every data type, {:.2f} to floats (2 digits
var1="Tuts"
my_string="the variable is {} and it belongs to {}".format(var,var1) # to add various data types to the same string

#NEWEST FORMATTING
my_string=f"the variabel is {var} and it belongs to {var1}" # more readeble, faster, what i've been using in my code



