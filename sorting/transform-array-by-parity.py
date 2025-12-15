class Solution(object):
    def transformArray(self, nums):
        evenNumber = 0
        oddNumber = 0
        for element in nums:
            if element % 2 == 0:
                evenNumber += 1
            else:
                oddNumber += 1
        return [0]*evenNumber + [1]*oddNumber