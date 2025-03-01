# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def same(self, left, right):
        if left is None or right is None:
            return left == right
        
        return left.val == right.val and self.same(left.left, right.right) and self.same(left.right, right.left)
    def isSymmetric(self, root):
        return self.same(root.left, root.right)