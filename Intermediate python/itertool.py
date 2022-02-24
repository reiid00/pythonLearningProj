# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
import operator
a=[1,2]
b=[3,4]
prod = product(a,b)
list(prod) # [(1, 3), (1, 4), (2, 3), (2, 4)] , prod is an iterator, combines a with b

b=[3]
prod = product(a,b,repeat=2)
list(prod) # [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)] , repeats, a with b 2 times

a=[1,2,3]
perm=permutations(a)
list(perm) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

perm=permutations(a,2) # second arg is length
list(perm) # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

a=[1,2,3,4]
comb = combinations(a, 3) # second arg is length
list(comb) # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

comb_wr=combinations_with_replacement(a, 2)
list(comb_wr) # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

acc=accumulate(a)
list(acc) # [1, 3, 6, 10], accumulates the values

acc_m=accumulate(a,func=operator.mul) # second argue can be the operator
list(acc_m) # [1, 2, 6, 24]

def smaller_then_3(x):
    return x<3

group_obj=groupby(a,key=smaller_then_3) # second argue is a function that is a comparison, returns values by True or False in lists
for key, value in group_obj:
    ey,list(value) # True [1, 2]
                   # False [3, 4]

