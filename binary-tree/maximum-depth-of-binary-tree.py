# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)

        return 1 + max(a,b)