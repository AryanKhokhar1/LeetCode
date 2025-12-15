class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        answer = []
        for ele in nums:
            num = 2*num + ele
            answer.append(num%5 == 0)
        return answer