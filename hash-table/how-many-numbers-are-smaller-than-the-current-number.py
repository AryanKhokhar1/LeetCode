class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*(max(nums)+1)
        for i in range(len(nums)):
            count[nums[i]] += 1

        for i in range(1,len(count)):
            count[i] += count[i-1]
        
        answer = []
        for ele in nums:
            if ele != 0:
                answer.append(count[ele-1])
            else:
                answer.append(0)
        return answer