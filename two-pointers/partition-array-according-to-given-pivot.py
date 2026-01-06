class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        for i in range(len(nums),0,-1):
            for j in range(1,i):
                print(nums)
                if nums[j] == pivot and nums[j-1] == pivot or nums[j] < pivot and nums[j-1] < pivot or nums[j] > pivot and nums[j-1] > pivot:
                    print("Same Category")
                    continue
                else:
                    print("Different Category",end=" ")
                    print(f"nums[j] = {nums[j]} and nums[j-1] = {nums[j-1]}")
                    if nums[j] < nums[j-1]:
                        nums[j],nums[j-1] = nums[j-1],nums[j]
                    
        print(nums)
        return nums