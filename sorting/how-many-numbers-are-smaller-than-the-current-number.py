class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortnums = sorted(nums)
        d = dict()
        for i in range(len(nums)):
            if d.get(sortnums[i]) == None:
                d[sortnums[i]] = i
        ans = []
        for ele in nums:
            ans.append(d.get(ele))
        return ans
