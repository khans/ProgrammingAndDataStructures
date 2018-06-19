#quick sort
'''
given: [3,5,2,1,0,3,6,9]
output: [0,1,2,3,3,5,6,9]
pivot is suppose a[mid]
'''
def quick_sort(given):
    if len(given)<=1:
        return given
    else:
        pivot = given[0]
        left=right=[]
        left = quick_sort([x for x in given[1:] if x < pivot])
        right = quick_sort([x for x in given[1:] if x >= pivot])
        return left+[pivot]+right  

print quick_sort([3,5,2,1,0,3,6,9])
''''
quick_sort([3,5,2,1,0,3,6,9])
[0, 1, 2, 3, 3, 5, 6, 9]
quick_sort([])
[]
quick_sort([0])
[0]
quick_sort([-2, -3])
[-3, -2]
'''