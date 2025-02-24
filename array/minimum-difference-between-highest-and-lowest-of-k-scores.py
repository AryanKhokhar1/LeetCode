class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        
        i = 0
        if len(nums) == 0:
            return 0
        diff = nums[-1]
        while i+k <= len(nums):
            diff = min(diff,nums[(i+k)-1] - nums[i])
            i += 1
        return diff

        