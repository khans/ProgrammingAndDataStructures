#[
#    [ 1, 2, 3 ],
#    [ 4, 5, 6 ],
#    [ 7, 8, 9 ]
#]
#Return [1,2,3,6,9,8,7,4,5]
class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        ## Actual code to populate result
        
        return result

B=[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ],
    [ 0, 0, 0 ]
]
A=[ [1,2],
    [3,4]
]

result = []
numElem = len(A)*len(A[0])
print numElem
rowsz = len(A[0])
rowind = rowsz-1
colsz = len(A)
cnt = 0

#number of rows is len(A) and number of columns is len(A[0])
while(len(result)!=numElem):
    i = 0; j=0;
    while(j<=rowind):
        result.append(B[i][j])
        j +=1
    
    
print result

    
