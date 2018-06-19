#https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
import sys
class Vertex():
    def __init__(self,node):
        self.id = node
        self.neighbors = []
    def addNeighbor(self,node1):
        v = Vertex(node1)
        self.neighbors.append(v)
        v.neighbors.append(self)
             
from collections import deque
class Graph():
    
    def __init__(self,n):
        self.vertices = {x : [] for x in range(n)}
        self.edges = []
        self.edgeLength = 6
   
    def connect(self,v1,v2):
        if v1!=v2:
            self.edges.append((v1,v2))
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)
            
    def find_all_distances(self,start):
      q = deque();
      q.append(start);
      
      distances = [-1 for x in range (len(self.vertices))]
      distances[start] = 0
      
      while(q):
        v = q.popleft();
        for each in self.vertices[v]:
          if distances[each] == -1:
            distances[each] = distances[v]+self.edgeLength
            q.append(each)
            
      return distances
               
 
        

t = int(input())        #No. of queries
for i in range(t):      # i will be 0,1,..t-1
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    d = graph.find_all_distances(s-1)
    for each in d:
        if each != 0:
            sys.stdout.write(str(each) + " ")
    print()
    
'''
Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
'''