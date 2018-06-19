def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]; distances = [-1 for x in range(len(graph))];
  
  edge = 6
  
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  print(distances)
  return path

def ispathBFS(graph, start,dest, path = []):
  '''iterative breadth first search from start'''
  q=[start]; 
  
  while q:
    v=q.pop(0)
    if v == dest:
      return True
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  
  return False

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'],
         'G': [] 
}
print iterative_bfs(graph, 'B', [])
print ispathBFS(graph,'A','G',[])

