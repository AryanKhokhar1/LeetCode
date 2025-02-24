# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def helper(tree):
            if tree is None:
                return 0
            
            a = helper(tree.left)
            b = helper(tree.right)
            self.diameter = max(self.diameter,(a+b))
            return 1+max(a,b)
        helper(root)
        return self.diameter