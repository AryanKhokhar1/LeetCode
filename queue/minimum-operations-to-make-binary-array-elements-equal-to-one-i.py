class Solution(object):
    def minOperations(self, nums):
        operation = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                operation += 1 
                nums[i] = 1
                nums[i+1] = (0 if nums[i+1] == 1 else 1)
                nums[i+2] = (0 if nums[i+2] == 1 else 1)
        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        else:
            return operation