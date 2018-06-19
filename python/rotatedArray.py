class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        if (n >0):
            low = 0
            high = n-1
            while (low <= high):
                if(A[low]<=A[high]):
                    return A[low]
                mid = low+ ((high-low)/2)
                nex = (mid+1)%n
                pre = (mid-1+n)%n
                if (A[nex] >= A[mid] and A[pre] >= A[mid]):
                    return A[mid]
                else:
                    if (A[mid]<=A[high]):
                        high = mid-1
                    if(A[mid]>= A[low]):
                        low  = mid+1
                