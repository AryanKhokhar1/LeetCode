# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxhelper(self,root):
        if root is None:
            return 0

        leftSum = max(self.maxhelper(root.left),0)
        rightSum = max(self.maxhelper(root.right),0)
        self.diameter = max(self.diameter, (leftSum + rightSum + root.val))
        return root.val + max(leftSum , rightSum)
    def maxPathSum(self, root):
        self.diameter = -1000
        self.maxhelper(root)
        return self.diameter