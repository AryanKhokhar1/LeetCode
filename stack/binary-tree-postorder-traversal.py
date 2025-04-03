# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        stack1 = [root]
        lis = []

        while len(stack1) != 0:

            ele = stack1.pop()    
            lis.append(ele.val)

            if ele.left:
                stack1.append(ele.left)
            if ele.right:
                stack1.append(ele.right)
        return lis[::-1]