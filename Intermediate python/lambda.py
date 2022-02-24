from functools import reduce

#lambda arguments: expression

#lambda way
add10= lambda x:x+10

#normal way
def add10_func(x):
    return x+10

add10(10) # 20

mult = lambda x,y:x*y

mult(2,3) # 6

points2D=[(1,2),(1,5),(1,-6),(12,-23),(10,20),(20,10),(-5,10)]

poinst2D_sorted = sorted(points2D) # sorts the list by X

points2D_sorted_lambdaY = sorted(points2D,key=lambda x:x[1]) # sorts the lists by Y using lambda function

points2D_sorted_lambdaSum = sorted(points2D,key=lambda x:x[0]+x[1])# sorts the lists by the sum of X and Y

# normal way of fucntion used on top
def sort_by_y(x):
    return x[1]

points2D # [(1, 2), (1, 5), (1, -6), (12, -23), (10, 20), (20, 10), (-5, 10)]
poinst2D_sorted # [(-5, 10), (1, -6), (1, 2), (1, 5), (10, 20), (12, -23), (20, 10)]
points2D_sorted_lambdaY # [(12, -23), (1, -6), (1, 2), (1, 5), (20, 10), (-5, 10), (10, 20)]
points2D_sorted_lambdaSum # [(12, -23), (1, -6), (1, 2), (-5, 10), (1, 5), (10, 20), (20, 10)]

#map(func,seq) seq is pe list
a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
list(b) # [2, 4, 6, 8, 10]

#list comprehension
c=[x*2 for x in a]
c # [2, 4, 6, 8, 10]

#filter(func,seq) func must return True or False, return all elems which the functions evaluates as true
b=filter(lambda x:x>3,a)
list(b) # [4, 5]

#list comprehension
c=[x for x in a if x>3]
c # [4, 5]

#reduce(func,seq) repeatedly returns the func to the elems and returns a single value

b = reduce(lambda x,y:x**2+y**2,a)
b # 1373609


