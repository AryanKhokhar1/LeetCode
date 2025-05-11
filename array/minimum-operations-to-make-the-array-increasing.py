class Solution(object):
    def minOperations(self, nums):
        if len(nums) == 1:
            return 0
        ans = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                ans += (nums[i]+1) - nums[i+1]
                nums[i+1] += (nums[i]+1) - nums[i+1]
        return ans


        