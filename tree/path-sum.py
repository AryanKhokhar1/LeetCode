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
            if root is None:
                if sum(psum) == targetSum:
                    return True
                else:
                    return False
            psum.append(root.val)

            if roottoleaf(root.left, psum, targetSum) or roottoleaf(root.right, psum, targetSum):
                return True
            psum.pop()
            return False

        return roottoleaf(root,[],targetSum)

        