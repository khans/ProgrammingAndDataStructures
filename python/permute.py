# Design an Algorithm to print all permutations of a string.
def perm(aStr):
  r = []
  if len(aStr)<=1:
    r = insert(aStr[0],r)
  elif len(aStr) == 2:
    r = insert(aStr[0],perm(aStr[1:]))
  else:
    r = insert(aStr[0],perm(aStr[1:]))
  return r
  
    

def insert(c,l):
  r = []
  if len(l) <1:
    r.append(c)
  else:
    for each in l:
      for j in range(len(each)+1):
        r.append(each[0:j]+c+each[j:])
  return r
  
print (perm('abc'))
    