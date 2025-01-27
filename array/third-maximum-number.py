class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = set(nums)
        nums = list(a)
        nums.sort()
        if(len(nums) < 3):
            return nums[-1]
        else:
            return nums[-3]