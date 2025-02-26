class Solution(object):
    def maxAbsoluteSum(self, nums):
        curr_max = 0
        maximum = -100000
        for ele in nums:
            curr_max += ele
            maximum = max(maximum, curr_max)
            curr_max = max(curr_max,0)
        
        neg_max = 0
        minimum = 100000
        for ele in nums:
            neg_max += ele
            minimum = min(minimum, neg_max)
            neg_max = min(neg_max, 0)
        return max(abs(minimum),maximum)