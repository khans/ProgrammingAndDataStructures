
from sys import maxsize
INF = maxsize
stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

class Result():
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.profit = -INF

def get_max_profit(s):
  mini = Result(-1,-1)
  pp = -INF
  x = -1; y = -1
  cp = 0
  t = []
  for i in range(len(s)-1):
    cp = s[i+1]-s[i]
    if mini.profit < 0:
      mini.profit = cp
      mini.x = i;
      mini.y = i+1
    else:
      mini.profit += cp
      mini.y = i+1
    if mini.profit > pp:
      pp = mini.profit
      x = mini.x;
      y = mini.y;
  return (pp,x,y)

def greedyMax(s):
  if len(s)<2:
    raise IndexError("Need atleast two values, need to buy before selling")
  minPrice = s[0]; maxProfit = s[1]-s[0]; start = 0; end = 1;
  for index,cp in enumerate(s):
    if index == 0:
      continue
    potentialProfit = cp - minPrice
    maxProfit = max(potentialProfit,maxProfit)
    if maxProfit == potentialProfit:
      end = index
    minPrice = min(cp,minPrice)
    if minPrice == cp and index<len(s)-1:
      start = index
  return (maxProfit,start,end)
    
print(get_max_profit([10,7,5,8,11,9]))
#3[-3, -2, 3, 3, -2]
print get_max_profit([1,-10,-7,-5,-11])
#[3, 2, -6]    

assert( greedyMax([10,7,5,8,11,9]) == (6,2,4)) 
assert( greedyMax([1,-10,-7,-5,-11]) == (5,1,3))

    

print(greedyMax([10,7,5,8,11,9]))
#3[-3, -2, 3, 3, -2]
print greedyMax([1,-10,-7,-5,-11])
#[3, 2, -6]    
 
   
