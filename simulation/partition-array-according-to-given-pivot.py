class Solution(object):
    def pivotArray(self, nums, pivot):
        leftNums = []
        rightNums = []
        pivotNums = []
        for ele in nums:
            if ele < pivot:
                leftNums.append(ele)
            elif ele > pivot:
                rightNums.append(ele)
            else:
                pivotNums.append(ele)
        return leftNums + pivotNums + rightNums