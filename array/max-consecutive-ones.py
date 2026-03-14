class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        OnesCount = 0
        maxCount = 0
        for ele in nums:
            if ele == 1:
                OnesCount +=1
            else:
                maxCount = max(maxCount,OnesCount)
                OnesCount = 0
        maxCount = max(maxCount,OnesCount)
        return maxCount
        

