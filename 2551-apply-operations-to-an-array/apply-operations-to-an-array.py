class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
        temp = [0]*len(nums)
        i = 0
        for ele in nums:
            if ele != 0:
                temp[i] = ele
                i +=1
        return temp