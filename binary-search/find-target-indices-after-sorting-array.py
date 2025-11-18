class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lis = []
        nums.sort()
        self.binarySearch(nums,0,len(nums)-1,target,lis)
        return lis
    def binarySearch(self,nums,left,right,target,lis):
        if left > right:
            return 
        
        mid = left + (right - left) // 2
        if nums[mid] == target:
            self.binarySearch(nums,mid+1,right,target,lis)
            self.binarySearch(nums,left,mid-1,target,lis)
            lis.append(mid)
        elif nums[mid] < target:
            return self.binarySearch(nums,mid+1,right,target,lis)
        else:
            return self.binarySearch(nums,left,mid-1,target,lis)