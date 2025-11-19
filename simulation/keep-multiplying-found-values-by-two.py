class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        found = True
        while(found):
            found = False
            for ele in nums:
                if ele == original:
                    original *= 2
                    found = True
                    break
        return original