class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -sys.maxsize -1
        curr_max = 0
        for ele in nums:
            curr_max += ele
            answer = max(answer, curr_max)
            curr_max= max(curr_max, 0)
        return answer