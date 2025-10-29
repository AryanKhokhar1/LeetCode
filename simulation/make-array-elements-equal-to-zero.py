class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        prefixSum = []
        answer = 0
        prev = 0
        for ele in nums:
            prev += ele
            prefixSum.append(prev)
        # if even both directional
        if prefixSum[-1] % 2 == 0:
            incre = True
            prev = 0
            for ele in prefixSum:
                if prev == ele:
                    incre = False
                else:
                    incre = True
                prev = ele
                if (ele + ele == prefixSum[-1]) and (not incre):
                    answer += 1
            answer = answer + answer
        else:
            incre = True
            prev = 0
            for ele in prefixSum:
                if prev == ele:
                    incre = False
                else:
                    incre = True
                prev = ele
                if (ele + ele == prefixSum[-1] or ele + ele == prefixSum[-1] + 1 or ele + ele == prefixSum[-1]-1) and (not incre):
                    answer += 1
        
        return answer