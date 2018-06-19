# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        x = A
        y = A
        return self.isSymmUtil(x,y)
        
    def isSymmUtil(self, x,y):
        if (x == None and y == None):
            return 1
        elif ((x != None and y == None) or (x == None and y != None)):
            return 0
        else:
            if(x.val==y.val and self.isSymmUtil(x.left,y.right) and self.isSymmUtil(x.right,y.left)):
                return True
            else:
                return False