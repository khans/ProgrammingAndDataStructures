# Print stuff in spiral way
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        r = len(A)
        c = len(A[0])
        if (r ==0 and c==0):
            return A[0]
        if (r ==1 and c==1):
          return A[0]
        n = r*c
        k = 0; z = 1; x=0; y=0; i = 0;
        while(i<n):
            while (y<c-1 and i<n):
                result.append(A[x][y])
                i += 1
                y += 1
            c -= 1
            while (x<r-1 and i<n):
                result.append(A[x][y])
                i += 1
                x += 1
            r -= 1
            while (y !=k and i<n):
                result.append(A[x][y])
                i += 1
                y -= 1
            k += 1
            while (x != z and i<n):
                result.append(A[x][y])
                i += 1
                x -= 1
            z += 1
            
        
        return result
r = Solution()
print (r.spiralOrder([[1]]))
print (r.spiralOrder(
[[1, 2,9,7,6,8],
[3, 4,13,45,0,88],
[5, 6,23,20,-1,98],
[15,16,17,18,19,90]
]))