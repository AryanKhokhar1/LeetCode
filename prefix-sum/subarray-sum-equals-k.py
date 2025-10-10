class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        for i in range(len(nums)+1):
            for j in range(i+1):
                if sum(nums[j:i]) == k:
                    ans += 1
        return ans