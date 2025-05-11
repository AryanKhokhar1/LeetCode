class Solution(object):
    def minOperations(self, nums):
        if len(nums) == 1:
            return 0
        ans = 0
        num = nums[0]
        for i in range(1,len(nums)):
            if num >= nums[i]:
                diff = (num+1) - nums[i]
                ans += diff
                num = nums[i]+ diff
            else:
                num = nums[i]
        return ans


        