class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = dict()
        duplicate_number = None
        for ele in nums:
            if d.get(ele) != None:
                duplicate_number = ele
            else:
                d[ele] = 1
        setNum = set(nums)
        for i in range(1,len(nums)+1):
            if i not in setNum:
                return [duplicate_number,i]
        return []


