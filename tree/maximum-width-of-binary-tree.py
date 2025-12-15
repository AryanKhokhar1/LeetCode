# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        root.val = 0
        queue = [root]
        mainlis = []
        while queue:
            l = len(queue)
            lis = []
            for i in range(l):
                ele = queue.pop(0)
                lis.append(ele.val)
                if ele.left:
                    ele.left.val = ele.val*2
                    queue.append(ele.left)
                if ele.right:
                    ele.right.val = (ele.val*2)+ 1
                    queue.append(ele.right)     
            mainlis.append(lis)      
        maxDiff = 0
        print(mainlis)
        for sublis in mainlis:
            maxDiff = max((sublis[-1] - sublis[0])+1,maxDiff)
        return maxDiff