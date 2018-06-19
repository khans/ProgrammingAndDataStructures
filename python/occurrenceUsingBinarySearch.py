class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        firstIndex = self.binarySearch(A,B,True)
        lastIndex = self.binarySearch(A,B,False)
        return (lastIndex-firstIndex+1)
        
    @classmethod    
    def binarySearch(self,A,B,ch):
      res = -1
      low = 0; high = len(A)-1
      while (low <= high):
        mid = low+((high-low)//2)
        if A[mid] == B:
          res = mid
          if(ch):
            high = mid-1  #Go on searching in the lower array
          else:
            low = mid+1   #Go on searching in the higher array
        elif A[mid] < B:
          low = mid+1
        else:
          high = mid-1
      
      return res
    
s = Solution()
A = (2,3,5,5,5,5,5,5,7,8)
B = 5
print (s.findCount(A,B))