from sys import maxsize
INF = maxsize

class Solution():
  
  def __init__(self,capacity):
    self.capacity = capacity
    self.weights = []
    self.values  = []
    self.array = []
    self.number = 0
    
  def addWtVal(self,wt,val):
    self.weights.append(wt)
    self.values.append(val);
    self.number += 1
  
  def memoize(self):
    self.array = [[-INF for x in range(self.capacity+1)] for y in range (self.number)]
    self.choices = [-1 for x in range(self.capacity+1)]
    #print (self.array)
    
  def knapsack(self,n,C):
    return self.knapsackUtil(n-1,C)
  
  def knapsackUtil(self, index, C):
    if (self.array[index][C] != -INF):
      return self.array[index][C]
    if (index < 0 or C == 0):
      res =  0;
    elif self.weights[index] > C:
      res = self.knapsackUtil(index-1, C)
    else:
      #you either don't choose or choose
      choice1 = self.knapsackUtil(index-1,C)
      choice2 = self.values[index] + self.knapsackUtil(index-1, C-self.weights[index])
      res = max(choice1,choice2)
      if res == choice2:
        self.choices[C] = index
    
    self.array[index][C] = res  
    return res
  
        
      

s = Solution(7)
s.addWtVal(1,1)
s.addWtVal(3,4)
#s.addWtVal(4,5)
#s.addWtVal(5,7)

s.memoize();
print(s.knapsack(2,7))
print(s.array)
print(s.choices)
