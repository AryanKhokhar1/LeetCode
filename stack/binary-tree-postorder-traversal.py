# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        stack = [root]
        postorder = []

        while stack:
            val = stack.pop()
            if val is None:
                continue
            postorder.append(val.val)
            if val.left:
                stack.append(val.left)
            if val.right:
                stack.append(val.right)
        return list(reversed(postorder))