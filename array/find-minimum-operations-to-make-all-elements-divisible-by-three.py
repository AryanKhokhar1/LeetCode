class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for ele in nums:
            if ele%3 != 0:
                count += 1
        return count