# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        if root != None:
            self.invert(root)
        return root
    
    def invert(self,A):
        temp =A.left
        A.left = A.right
        A.right = temp
        
        if (A.left != None):
            self.invert(A.left)
        
        if (A.right != None):
            self.invert(A.right)   
            
            
# We first exchange 
#the initial left and right nodes, then we go in each of the nodes and reverse their left and right nodes
            
        