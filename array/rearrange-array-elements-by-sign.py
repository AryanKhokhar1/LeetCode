class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # with the help of two pointer approach
        i,j = 0,1
        while i < len(nums):
            if nums[i] >= 0:
                i += 2
            elif nums[j] < 0:
                j += 2
            else:
                nums[i],nums[j] = nums[j],nums[i]
                i+=2
                j+=2
        return nums