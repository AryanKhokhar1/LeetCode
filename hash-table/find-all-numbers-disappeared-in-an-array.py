class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setNum = set(nums)
        ans = []
        for i in range(1,len(nums)+1):
            if i not in setNum:
                ans.append(i)
        return ans