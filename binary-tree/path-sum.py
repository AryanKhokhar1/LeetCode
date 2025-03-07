# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        def roottoleaf(root,psum,targetSum):
            if root.left is None and root.right is None:
                if sum(psum) == targetSum:
                    print(psum)
                    return True
                else:
                    return False
            if root.left:
                psum.append(root.left.val)
                if roottoleaf(root.left, psum,targetSum):
                    return True
                psum.pop()
            if root.right:
                psum.append(root.right.val)
                if roottoleaf(root.right, psum, targetSum):
                    return True
                psum.pop()
            return False
        return roottoleaf(root,[root.val],targetSum)