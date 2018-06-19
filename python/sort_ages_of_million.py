'''
Program to sort an array of numbers, where the array is a list of integers that 
ages of a million customers.

Given: an array of a million customers's ages
To do: Sort the array
Note: This program will only work for positive numbers only.
'''

def sortarr(given):
    l = []
    for i in range(0,131):
        l.append(0) #list of 130 items initialized
    
    for each in given: # each will represent the index in l
        l[each]=l[each]+1
    #print l
    
    #sorting the input list:
    i=j=0
    while i<=130:      #traversing the list l 
        if l[i]!=0:    
            k = 0
            while k<l[i]:
                given[j] = i
                j +=1
                k +=1
            i +=1
        else:
    
            i +=1
    return given
    
print sortarr([130,34,67,90,2,34,67,29,37,130,0])
print sortarr([])

        