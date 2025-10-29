class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefixSum = []
        answer = 0
        prev = 0
        for ele in nums:
            prev += ele
            prefixSum.append(prev)
        if prefixSum[-1]%2 != 0:
            return answer
        else:
            half = prefixSum[-1]//2

        for ele in prefixSum:
            if half == ele:
                answer += 1
        
        return answer