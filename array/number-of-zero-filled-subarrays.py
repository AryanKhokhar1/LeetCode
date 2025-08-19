class Solution(object):
    def zeroFilledSubarray(self, nums):
        occurance = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if sum(nums[i:j]) == 0:
                    occurance += 1        
        return occurance