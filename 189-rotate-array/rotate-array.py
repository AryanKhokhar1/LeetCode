class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = dict()
        l = len(nums)
        for index, value in enumerate(nums):
            d[index] = value
        for i in range(len(nums)):
            nums[(i+k)%l] = d[i]
        
        