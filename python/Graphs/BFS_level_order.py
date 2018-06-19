g={1: [2, 3,6], 2: [4, 5], 3: [6, 7],4:[8,9,13]}


def BFS(G,root):
    queue = []     #The queue
    visited = []   #The path of visited nodes
    ht = [(0,root)]
    #Starting:
    queue.append(root)
    level = 1
    members = 1
    neighbors = 0
    ht = [(0,root)]
    
    while queue != []:
        v = queue.pop(0)        
              
        # if no members on current level then go to the children
        if members == 0:
            members = neighbors
            neighbors = 0
            level += 1
        queue = queue + G.get(v,[]) #append children of root initially
        if members > 0:  #initially members is 1 so we decrement it
            members -= 1
            for each in G.get(v,[]): # 
                neighbors += 1
                ht.append((level,each))
        
        visited.append(v)  #Path 
        
    prevLevel=None
        
    for v,k in sorted(ht):
        if prevLevel!=v:
            if prevLevel!=None:
                print "\n"
        prevLevel=v
        print k,        
    return ht  
        
        
            
    



'''
1 

2 3 6 

4 5 6 7 

8 9 13
'''
    
    
    