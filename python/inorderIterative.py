# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        if A == None:
            return []
        elif(A.left ==None and A.right == None):
            return [A.val]
        else:
            stack = [A]
            ans = []
            B = A; C = A
            while(stack):
                while (B != None):
                    B = B.left
                    if B != None:
                        stack.append(B)
                if B == None:
                    B = stack[-1]
                    stack.pop()
                    ans.append(B.val)
                    if B.right != None:
                        stack.append(B.right)
                    B = B.right
        return ans
'''
    def inorderTraversal(self, A):
        if A == None:
            return []
        elif(A.left ==None and A.right == None):
            return [A.val]
        else:
            stack = [A]
            ans = []
            B = A; C = A
            while(stack):
                if B!=None:
                    B = B.left
                if B != None:
                    stack.append(B)
                if B == None:
                    B = stack[-1]
                    stack.pop()
                    ans.append(B.val)
                    if B.right != None:
                        stack.append(B.right)
                    B = B.right
        
        return ans
'''