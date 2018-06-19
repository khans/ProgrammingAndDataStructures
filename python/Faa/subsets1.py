import sys

class Solution:
  def print_set(self,res):
    #sys.stdout.write('{')
    print (res)
    #for i in range(len(res)):
     # if res[i] != None:
      #  sys.stdout.write(str(res[i]))
        
       # if (i+1) <len(res):
          #print (res[i+1])
        #if i+1 <len(res) and res[i+1] != None:
          
        #sys.stdout.write(',')
    #sys.stdout.write('}')
    #print()

  def print_comb(self,given):
    res = [None]*len(given)
    self.helper(given, res, 0, len(given))
  
  def helper(self,given,res,i, n):
    if i== n:
      self.print_set(res)
    else:
      res[i] = None
      self.helper(given,res,i+1,n)
      res[i] = given[i]
      self.helper(given,res,i+1,n)
      
    
    
s = Solution()
s.print_comb([1,2,3])