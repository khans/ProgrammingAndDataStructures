def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs_queue(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path
  

def iterative_dfs_stack(graph, start, path=[]):
  '''iterative depth first search from start'''
  s=[start]
  while s:
    v=s.pop()
    if v not in path:
      path=path+[v]
      s=s+graph[v]
  return path
    

def rec(g,start,dest,visited = {},path=[]):
  print (start,dest,visited,path)
  if start in visited:
    return (False,path)
  
  visited.update({start:1})
  path += [start]
  if start == dest:
    return (True,path)
  
  for node in g[start]:
    if rec(g,node,dest,visited,path):
      #print (start,dest,visited,path)
      return (True,path)
     
  return (False,path)
  
  
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
#print iterative_dfs_queue(graph, 'A', [])
#print iterative_dfs_stack(graph, 'A', [])
#print recursive_dfs(graph, 'A', [])
#print rec(graph, 'A','F', {},[])

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    print(stack)
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if not neighbor in visited:
                  stack.append((neighbor, path + [neighbor]))
                print (stack)

print (dfs_paths(graph, 'A', 'F'))  