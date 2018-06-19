#Python script or permutations

#Following procedure is for n==2, if l=[0,1] then returns [[0,1],[1,0]]
def perms_for_2(l):
    perm = []
    s=[]
    for each in l:
        s.append(each)
    perm.append(s)
    s=[]
    for each in reversed(l):
        s.append(each)            
    perm.append(s)
    return perm    

#Following procedure is for n>2, 
def perms_for_more(l,chopped):   
    temp = []
    answer = []
    for each in l:
        for i in range(0,len(each)+1):
            temp = list(each)
            temp.insert(i,chopped)
            answer.append(temp)
    return answer
            

def permutations(l):
    #l is the list and r is the types of arrangements
    n = len(l)
    if n<=1:
        return l
    elif n==2:
        return perms_for_2(l)
         
    elif n>2:
        answer = []
        chopped = l[-1]
        return perms_for_more(permutations(l[:n-1]),chopped)
    
    
        
print permutations([1,2,3])


    
            
        
        
    
