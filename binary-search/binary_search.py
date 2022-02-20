import random,time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l,target):
    low=0
    high=len(l)-1
    return binary_search1(l, target, low, high)

def binary_search1(l,target,low,high):
    if high<low:
        return -1
    midpoint =  (low+high) // 2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:
        return binary_search1(l, target,midpoint+1,high)
    else:
        return binary_search1(l, target,low,midpoint-1)


if __name__ == '__main__':
    print('Comparison between naive and binary search \n')
    length=int(input('Length of list: '))
    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-3*length,3*length))
    sorted_list = sorted(list(sorted_list))
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f'Naive search time: {(end-start)/length} seconds')
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f'Binary search time: {(end-start)/length} seconds')