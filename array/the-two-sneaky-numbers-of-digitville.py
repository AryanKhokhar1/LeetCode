class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = dict()
        ans = []
        for ele in nums:
            if d.get(ele) == None:
                d[ele] = True
            else:
                ans.append(ele)
        return ans