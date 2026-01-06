class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        answer = 50
        for i in range(len(nums)//2):
            answer = min(answer, (nums[i] + nums[-i-1])/2)
        return answer