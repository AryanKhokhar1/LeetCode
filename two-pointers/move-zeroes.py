class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for element in nums:
            if(element == 0):
                count += 1
        for _ in range(count):
            nums.remove(0)
        for _ in range(count):
            nums.append(0)