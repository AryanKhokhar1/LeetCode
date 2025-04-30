class Solution(object):
    def findNumbers(self, nums):
        ans = 0
        for ele in nums:
            if len(str(ele))%2 == 0:
                ans += 1
        return ans        