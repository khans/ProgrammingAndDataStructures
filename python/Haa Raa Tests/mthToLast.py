class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    def add(self,node):
        self.next = node
        
        
def x(M,l):
    n = 1
    root = Node(l.pop(0))
    prev = root
    while(l):
        n += 1
        curr = Node(l.pop(0))
        prev.next = curr
        prev = curr
    if M > n:
        print ('NIL')
    else:
        diff = n-M
    print(n,M)
    
    curr = root
    while(curr):
      print(curr.val)
      curr = curr.next
    
    prev = root
    curr = root
    i = 0
    while(curr and i<=diff):
        i += 1
        prev = curr
        curr = curr.next
    print (prev.val)
# x(3,[1,2,3,4,5,6,7,8])


T = int(input())        #tescases
for i in range(T):
    M = int(input())
    L = input()
    #Split L and put into linked list
    l = [int(x) for x in L.split()]
    x(M,l)