# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self,root,pre):
        if root is None:
            return 
        pre.append(root.val)
        self.preorder(root.left,pre)
        self.preorder(root.right,pre)
        return pre
    def inorder(self,root,ino):
        if root is None:
            return
        self.inorder(root.left,ino)
        ino.append(root.val)
        self.inorder(root.right,ino)
        return ino

    def postorder(self,root,post):
        if root is None:
            return
        self.postorder(root.left,post)
        self.postorder(root.right,post)
        post.append(root.val)
        return post
    def isSameTree(self, p, q):
        
        return self.preorder(p,[]) == self.preorder(q,[]) and self.inorder(p,[]) == self.inorder(q,[]) and self.postorder(p,[]) == self.postorder(q,[])
        
        