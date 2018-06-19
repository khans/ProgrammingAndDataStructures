class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
      if len(A) == 0:
        return 0
      else:
        cnt = 0
        low = 0; high = len(A)-1;
        while(low<=high):
          mid = int(low +(high-low)/2)
          if (B == A[mid]):
            return mid
          elif(B<A[mid]):
            high = mid-1
          elif(B>A[mid]):
            low = mid+1
        return -1
        

s = Solution();
A = (5,5,5,5,5,5,5,5,8)
B = 9
print(s.findCount(A,B))