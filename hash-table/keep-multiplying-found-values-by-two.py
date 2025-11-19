class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d = dict()
        for ele in nums:
            if d.get(ele) == None:
                d[ele] = True
        found = True
        while(found):
            if d.get(original) == True:
                original *= 2
            else:
                found = False
        return original
