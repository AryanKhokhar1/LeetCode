class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for ele in nums:
            if ele in s:
                ans.append(ele)
            else:
                s.add(ele)
        return ans