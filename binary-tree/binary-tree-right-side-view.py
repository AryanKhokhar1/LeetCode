# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        self.d =dict()
        self.queue = [[root,0]]
        def bfs():
            if not self.queue:
                return
            ele = self.queue.pop(0)
            self.d[ele[1]] =ele[0].val
            if ele[0].left:
                self.queue.append([ele[0].left,ele[1]+1])
            if ele[0].right:
                self.queue.append([ele[0].right,ele[1]+1])
            return bfs()
        bfs()
        return [self.d[k] for k in sorted(self.d.keys())]
        