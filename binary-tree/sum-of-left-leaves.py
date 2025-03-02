# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.summ = 0

        def helper(root,l):
            if root is None:
                return
            if root.left is None and root.right is None and l:
                self.summ += root.val
            helper(root.left, True)
            helper(root.right,False)

        helper(root,False)
        return self.summ
        