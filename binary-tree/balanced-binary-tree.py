# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalancedhelper(self, root):
        if root is None:
            return 0
        
        a = self.isBalancedhelper(root.left)
        b = self.isBalancedhelper(root.right)

        if a == -1 or b == -1: return -1
        if abs(a-b)> 1: return -1
        return 1+max(a,b)

    def isBalanced(self, root):
        return self.isBalancedhelper(root) != -1
        