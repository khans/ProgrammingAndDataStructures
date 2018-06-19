# Tree Node definition with an insert function in the Class
class Node:
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None
  def insert(self,root,val):
    if root is None:
      root = Node(val)
    elif (val < root.val):
        if root.left is None:
          root.left = Node(val)
        else:
          self.insert(root.left,val)
    else:
      if root.right is None:
        root.right = Node(val)
      else:
        self.insert(root.right,val)

# Calculating the distance between two nodes: Distance to node1 + Distance to node 2 - 2*(Distance to LCA)
def bstDistance(values, n, n1, n2):        
  if n1 not in values or n2 not in values:
    return -1
  root = Node(values[0])
  for i in range (1,n):
    root.insert(root,values[i])
  '''print (root.val)
  print (root.left.val)
  print (root.right.val)
  print (root.left.left.val)
  print (root.left.right.val)
  print (root.left.left.right.val)
  '''
  s = 0
  x = pathlength(root,n1,s)-1
  print(x)
  s = 0
  y = pathlength(root,n2,s)-1
  print(y)
  lca = findLCA(root,n1,n2)
  s = 0
  lcaD = pathlength(root,lca.val,s)-1
  print(lcaD)
  return (x+y)-(2*lcaD)
  

#Calculate length of the path
def pathlength(root,val,x):
  if root == None:
    return 0
  else:
    if val == root.val:
      return x+1
    elif val < root.val:
      x = pathlength(root.left,val,x+1)
    else:
      x = pathlength(root.right,val,x+1)
    if x>1:
      return x
    else:
      return 0

# find the LCA
def findLCA1(root,val1,val2):
  if root is not None:
    if val1 > root.val and val2 >root.val:
      return findLCA(root.right,val1,val2);
    if val1 < root.val and val2 <root.val:
      return findLCA (root.left,val1, val2)
    return root
  return None
#Another way
def findLCA(root,val1,val2):
  while (root is not None):
    if val1 > root.val and val2 >root.val:
      root = root.right
    elif val1 < root.val and val2 <root.val:
      root = root.left
    else:
      break
  return root
    

values = [5,6,3,1,2,4]
n = len(values)
node1 = 1;
node2 = 6;
print (bstDistance(values, n, node1, node2)) 