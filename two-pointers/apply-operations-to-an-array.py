class Solution(object):
    def applyOperations(self, nums):
        if len(nums) <= 1:
            return nums
        if nums[0] == nums[1]:
            nums[0] = 2 * nums[0]
            nums[1] = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = 2*nums[i-1]
                nums[i] = 0
        leftLis = []
        numberZero = []
        for ele in nums:
            if ele == 0:
                numberZero.append(0)
            else:
                leftLis.append(ele)
        return leftLis + numberZero