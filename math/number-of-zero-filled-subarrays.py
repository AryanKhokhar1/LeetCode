class Solution(object):
    def zeroFilledSubarray(self, nums):
        answer = 0
        occur = 0
        for ele in nums:
            if ele == 0:
                occur += 1
            else:
                if occur > 0:
                    answer += (occur * (occur + 1))/2
                    occur = 0
        if occur > 0:
            answer += (occur * (occur + 1))/2
        return answer