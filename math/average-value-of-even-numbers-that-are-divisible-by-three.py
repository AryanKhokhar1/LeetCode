class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0
        for ele in nums:
            if ele %6 == 0:
                ans += ele
        return ans //2