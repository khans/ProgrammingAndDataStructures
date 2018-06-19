def sortarr(given):
    l = []
    for i in range(0,131):
        l.append(0) #list of 130 items initialized
    
    for each in given: # each will represent the index in l
        l[each]=l[each]+1
    #print l
    
    #sorting the input list:
    i=j=0
    while i<=130:      #traversing the list l 
        if l[i]!=0:    
            k = 0
            while k<l[i]:
                given[j] = i
                j +=1
                k +=1
            i +=1
        else:
    
            i +=1
    return given
    
print sortarr([130,34,67,90,2,34,67,29,37,130,0])
print sortarr([])

#maximum subarray problem using Kadane's algorithm
import sys
class Result:
  def __init__(self,i,j,sum):
    self.i = i;
    self.j= j
    self.sum = sum
    

class Solution:
  def maxSub(self,A,n):
    negVal = -1*sys.maxsize
    maxi = Result(-1,-1,negVal);
    maxCurr = maxi
    res = []
    for i in range (0,n):
      if maxCurr.sum < 0:
        maxCurr.sum = A[i]
        maxCurr.i = i;
        maxCurr.j = i;
      else:
        maxCurr.sum += A[i]
        maxCurr.j = i
      if maxCurr.sum > maxi.sum:
        maxi = maxCurr
      res.append(maxi)
    #print (res[n-1].sum)
    return res[n-1]
      
    

s = Solution()
A = [-2,-1,3,4,-5,6]
B = [-2,-1]
print (s.maxSub(A,6).sum)
print (s.maxSub(B,2).sum)

# O(n^2) solution:
class Solution1:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if (len(A) == 1):
            return A[0]
        elif (len(A) == 0):
            return
        else:
            n = len(A)
            total = sum(A)
            tSum = total
            maxSum = total
            for i in range(0,n-1):
                for j in range (n-1,i,-1):
                    if(i==j):
                        break
                    else:
                        tSum = tSum - A[j]
                        maxSum = max(maxSum,tSum)
                tSum = total - A[i]
                total = tSum
                maxSum = max(maxSum,tSum)
            return maxSum