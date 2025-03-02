# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):

        if root is None:
            return []
        mainlis = []
        queue = [root]
        lefttoright = True
        while queue:

            lis = []
            l = len(queue)
            for i in range(l):

                val = queue.pop(0)
                lis.append(val.val)

                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
                
            if lefttoright:
                mainlis.append(lis)
            else:
                mainlis.append(list(reversed(lis)))
            
            lefttoright = not lefttoright
        return mainlis