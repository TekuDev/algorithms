#!/usr/bin/python3

array = [1,8,55,93,15,11,49,4,6,55,101,74,53,22,59]

def mergeSort(l):

    n = len(l)

    if n == 1:
        return l

    l1 = mergeSort(l[0 : int(n/2)])
    l2 = mergeSort(l[int(n/2) : n])

    return merge(l1, l2)

def merge(l1, l2):

    listMerged = []

    while (len(l1) > 0 and len(l2) > 0):

        if l1[0] < l2[0]:
            listMerged.append(l1[0])
            l1.pop(0)
        else:
            listMerged.append(l2[0])
            l2.pop(0)
    
    while (len(l1) > 0):
        listMerged.append(l1[0])
        l1.pop(0)
    
    while (len(l2) > 0):
        listMerged.append(l2[0])
        l2.pop(0)
    
    return listMerged

print(array)
array = mergeSort(array)
print(array)