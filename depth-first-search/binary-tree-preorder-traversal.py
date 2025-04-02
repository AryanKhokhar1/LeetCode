# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        answer = []
        while len(stack) != 0:
            ele = stack.pop()
            answer.append(ele.val)
            if ele.right:
                stack.append(ele.right)
            if ele.left:
                stack.append(ele.left)
        return answer