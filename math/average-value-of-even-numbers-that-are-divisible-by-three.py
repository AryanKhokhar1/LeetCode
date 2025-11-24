class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0
        n = 0
        for ele in nums:
            if ele %6 == 0:
                ans += ele
                n+= 1
        if n == 0:
            return 0
        return ans // n