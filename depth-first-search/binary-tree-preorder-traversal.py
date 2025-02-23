# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        stack = [root]
        preorder = []
        while stack:
            val = stack.pop()
            if val is None:
                continue
            preorder.append(val.val)

            if val.right:
                stack.append(val.right)
            if val.left:
                stack.append(val.left)
            
        return preorder
        