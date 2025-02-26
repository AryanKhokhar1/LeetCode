class Solution(object):
    def maxSubArray(self, nums):
        
        maxi = -100000
        curr_max = 0
        for ele in nums:
            curr_max += ele
            maxi = max(maxi, curr_max)        
            curr_max = max(curr_max, 0)
        return maxi