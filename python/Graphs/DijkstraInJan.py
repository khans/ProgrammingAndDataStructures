import heapq,sys
max = 10000000
graph = {'a':{'b':7,'c':3},'b':{'a':7,'c':1,'d':2,'e':6}, 
'c':{'a':3,'b':1,'d':2},'d':{'c':2,'b':2,'e':4},'e':{'b':6,'d':4}}



#set for all vertices
map = {x for x in graph}
#we keep popping this as soon as we pop our heap as well

start = 'a'
q = [[max,each] for each in graph if each != start]
q.append([0,start])



heapq.heapify(q)
pred = {}
dist = {}

while(q):
  min = heapq.heappop(q)

  vertex = min[1]
  map.remove(vertex)

  currd = min[0]

  if vertex == start:
    pred[vertex] = None

  for neighbor in graph[vertex]:
    if neighbor in map:
      td = currd+graph[vertex][neighbor]
      for each in q:
        if each[1] == neighbor and each[0] > td:
          each[0] = td
          pred[neighbor]=vertex
          dist[neighbor]=td
      else:
        continue
  heapq.heapify(q)
print(pred)   
print(dist)
    