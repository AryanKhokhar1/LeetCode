# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathfinder(self, root, path, target):
        if root is None:
            return False

        path.append(root)
        if root == target:
            return path
        
        if self.pathfinder(root.left, path, target) or self.pathfinder(root.right, path, target):
            return path
        
        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        pathp = self.pathfinder(root, [], p)
        pathq = self.pathfinder(root, [], q)
        minh = min(len(pathp),len(pathq))
        same = root
        for i in range(minh):
            if pathp[i].val != pathq[i].val:
                return same
            same = pathp[i]
        return same
        