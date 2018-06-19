''''
Quick sort with random selection of pivot
for random index we use randrange, for random value from a list we use choice
'''
from random import randrange,choice
def qsort(list): #Passing copy of list
    def qsort_copy(list):
        if list == []: 
            return []
        else:
            pivot = list.pop(randrange(len(list)))
            lesser = qsort_copy([l for l in list if l < pivot])
            greater = qsort_copy([l for l in list if l >= pivot])
            return lesser + [pivot] + greater
    return qsort_copy(list[:])

print qsort([3,5,2,1,0,3,6,9])