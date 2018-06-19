class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def AddNode(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        
        if self.tail != None:
            self.tail.next = new_node
        
        self.tail = new_node
    
    def RemNode(self,index):
        prev = None
        node = self.head
        i = 0
       
        while ( node != None ) and ( i < index ):
            prev = node
            node = node.next
            i += 1
       
        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next        
    
    def PrintList(self):
        node = self.head
        while node != None:
            print node.data
            node = node.next
            
            
#
List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(4)
List.PrintList( )

List.RemNode( 2 )
        
List.PrintList( )
'''
1
2
3
4
1
2
4
'''
