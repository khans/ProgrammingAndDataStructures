#merge-sort

def merge_sort(m):
    if len(m)<=1:
        return m
    left=right=[]
    mid = len(m)/2
    left = merge_sort(m[:mid])
    right = merge_sort(m[mid: ])
    return merge(left,right)

def merge(left,right):
    result = []
    i=j=0
    while(i<len(left))and (j<len(right)): 
        if(left[i]<right[j]):
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1
    result += left[i: ]
    result += right[j: ]
    return result
print merge_sort([2,3,6,7,9,0,-1,2])
#[-1, 0, 2, 2, 3, 6, 7, 9]
    
    
