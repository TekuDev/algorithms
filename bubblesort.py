#!/usr/bin/python3


array = [1,8,55,93,15,11,49,4,6,55,101,74,53,22,59]

def bubblesort(a):
	for i in range(0,len(a)-1):
		for j in range(i, len(a)):
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
	return a
    	


print(array)
array = bubblesort(array)
print(array)