# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.paths = []
        self.path = []
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return False
        
        self.path.append(root)

        if root == p:
            self.paths.append(self.path[:])
        if root == q:
            self.paths.append(self.path[:])
        if len(self.paths) == 2:
            l = min(len(self.paths[0]), len(self.paths[1]))
            m = self.paths[0][0]
            for i in range(l):
                if self.paths[0][i] == self.paths[1][i]:
                    m = self.paths[0][i]
                else:
                    return m
            return m
        
        left = self.lowestCommonAncestor(root.left,p,q)
        if left is not False:
            return left
        
        right = self.lowestCommonAncestor(root.right,p,q)
        if right is not False:
            return right
        
        self.path.pop()
        return False