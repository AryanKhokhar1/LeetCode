# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxhelper(self,root,diameter):
        if root is None:
            return 0

        leftSum = self.maxhelper(root.left , diameter)
        rightSum = self.maxhelper(root.right, diameter)
        self.diameter = max(self.diameter, (leftSum + rightSum + root.val))
        return root.val + max(leftSum , rightSum)
    def maxPathSum(self, root):
        self.diameter = 0
        self.maxhelper(root,self.diameter)
        return self.diameter