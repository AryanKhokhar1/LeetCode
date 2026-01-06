class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        numstore = {}
        ans = 0
        for ele in nums:
            if numstore.get(ele) == None:
                numstore[ele] = 1
        for ele in nums:
            # if ele+diff, ele+2*diff exist in nums means we found a triplet
            if numstore.get(ele+diff) != None and numstore.get(ele+diff+diff) != None:
                ans +=1
        return ans

