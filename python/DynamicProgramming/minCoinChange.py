from sys import maxsize
INF = maxsize
total = 13
coins = [7,4,2]

def minCoins(total,coins):
  combinations = []
  #create two lists of length total+1 
  T = [INF] * (total+1)
  T[0] = 0
  
  C = [-1] * (total+1)
  
  for j in range(0,len(coins)):
    for i in range(1,total+1):
      
      if i < coins[j]:
        continue
      prev = T[i]
      T[i] = min(T[i], 1+T[i-coins[j]])
      
      if T[i] != prev:
        C[i] = j;
    #before you increment j check if the last element of C is not -1 and then append to combinations
    if C[i] != -1:
      innerList = traverseCurrCoins(C,coins)
      combinations.append(innerList)
    
  print (combinations)
  print (C)
  print (T[-1])
  return;
  
  
def traverseCurrCoins(C,coins):
  chosen = [];
  k = total
  while(k!=0):
    value = coins[C[k]]
    chosen.append(value)
    k = k - value
  return chosen
        
minCoins(total, coins)