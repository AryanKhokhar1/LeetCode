class Solution(object):
    def maxDepth(self, s):
        ans = 0
        isBalance = 0
        for ele in s:
            if ele == "(":
                isBalance += 1
                ans = max(isBalance, ans)
            elif ele == ")":
                isBalance -= 1
        return ans