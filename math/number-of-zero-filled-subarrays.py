class Solution(object):
    def zeroFilledSubarray(self, nums):
        occurance = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                check = True
                for ele in nums[i:j]:
                    if ele != 0:
                        check = False
                        break
                if check:
                    occurance += 1
        return occurance