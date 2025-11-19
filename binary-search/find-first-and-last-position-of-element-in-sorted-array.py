class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(target,nums)
        if left == len(nums) or nums[left] != target:
            return [-1,-1]
        right = self.binarySearch(target+1, nums)
        return [left,right-1]
    def binarySearch(self,target,lis):
        start,end = 0,len(lis)
        while(start < end):
            mid = start + (end - start)//2
            if lis[mid] < target:
                start = mid + 1
            else:
                end = mid 
        return start