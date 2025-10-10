class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        
        prefixnums = []
        total = 0
        for ele in nums:
            total += ele
            prefixnums.append(total)
        
        ans = 0
        for i in range(len(nums)):
            start = max(0, i-nums[i])

            if start == 0:
                ans += prefixnums[i]
            else:
                ans += (prefixnums[i] - prefixnums[start-1])
        return ans