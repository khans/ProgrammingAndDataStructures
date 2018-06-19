capacity = 7
w = [1,3,4,5]
v = [1,4,5,7]

T =[[0 for x in range (capacity+1)] for y in range (len(w))]
C = [-1 for x in range (capacity + 1)]
for i in range (len(w)):
  for j in range (1,capacity+1):
    
    if j < w[i] and i>0:
        T[i][j] = T[i-1][j]
   
    else:
      prev = T[i][j]
      if i == 0:
        T[i][j] = v[i]
      else:
        T[i][j] = max(T[i-1][j], v[i]+T[i-1][j-w[i]])
      if T[i][j] != prev:
        C[j] = i