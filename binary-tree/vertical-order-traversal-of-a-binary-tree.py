# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalhelper(self, root, lr, v):
        if root is None:
            return 
        self.lis.append([lr,v,root.val])
        self.verticalhelper(root.left, lr-1, v+1)
        self.verticalhelper(root.right, lr+1, v+1)
    def verticalTraversal(self, root):
        self.lis = list()
        self.verticalhelper(root, 0, 0)
        self.lis.sort()
        answer = []
        sub = []
        start = self.lis[0][0] 
        for i in range(len(self.lis)):
            if start == self.lis[i][0]:
                sub.append(self.lis[i][2])
            else:
                answer.append(sub)
                sub = list()
                sub.append(self.lis[i][2])
                start = self.lis[i][0]
        answer.append(sub)
        return answer