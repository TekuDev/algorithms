#!/usr/bin/python3

import random

#array = [1,9,5,7,11,36,2,5,9,45,0,21]
array = [1,8,55,93,15,11,49,4,6,55,101,74,53,22,59]

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part


print(array)
array = quicksort(array)
print(array)