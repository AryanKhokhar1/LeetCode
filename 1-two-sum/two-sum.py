class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            d[value] = index
        for i in range(len(nums)):
            v = d.get(target-nums[i])
            if v and v != i:
                return [i,v]
        