import heapq,sys

iGraph = {'A':{'B': 4,'C':2}, 'B':{'A':4,'D':3,'C':5}, 'C':{'A':2,'D':10}, 'D':{'C':10,'B':3}}
Graph = {'A':{'B': 5,'D':9,'E':2}, 'B':{'A':5,'C':2}, 'C':{'B':2,'D':3}, 'D':{'C':3,'A':9,'F':2}, 'E':{'A':2,'F':3},'F':{'E':3,'D':2}}

g = []

class Vertex():
  def __init__(self,node):
    self.id = node
    self.distance = sys.maxsize
    
Graph1 = {Vertex('A'):{Vertex('B'): 4,Vertex('C'):2}, Vertex('B'):{Vertex('A'):4,Vertex('D'):6}, Vertex('C'):{Vertex('A'):2,Vertex('D'):10}, Vertex('D'):{Vertex('C'):10,Vertex('B'):6}}    

for each in Graph:
    if each == 'A':
      heapq.heappush(g,(0,each))
    else:
      heapq.heappush(g,(sys.maxsize,each))


  

def shortestPath(graph,start,end):
  path = []
  pred = {}
  distances = {}
  prev = None
  
  queue = [[Vertex(v).distance,Vertex(v)] for v in graph if v != start]
  s = Vertex(start)
  s.distance = 0;
  
  queue.append([s.distance,s])
  heapq.heapify(queue)
  i = 0
  while(queue):
    print ('iteration is %d'%i)
    minimum = heapq.heappop(queue)
    print (minimum[1].id)
    curr = minimum[1]   #Vertex
    distances[curr.id] = curr.distance
    
    for each in queue:
      if (each[1].id in graph[curr.id]):
        print (each[1].id + ' is in ' + curr.id)
        pred[each[1].id] = curr.id
        newDist = curr.distance + graph[curr.id][each[1].id]
        if newDist < each[0]:
          each[1].distance = newDist
          each[0]= each[1].distance
          distances[each[1].id] = each[1].distance
    print (queue)
    i += 1
    
    
  print(queue)
  print(pred)
  print (distances)
  
  
  while(end != start):
    print(end)
    path.insert(0,end)
    end = pred[end]
  path.insert(0,start)
  print (path)
shortestPath(Graph,'A','B')




  
  