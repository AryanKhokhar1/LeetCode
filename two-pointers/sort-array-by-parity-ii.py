class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            if ((i%2 == 0 and nums[i]%2!=0) or (i%2 != 0 and nums[i]%2 == 0)) and (j%2 != 0 and nums[j]%2 == 0) or (j%2 == 0 and nums[j]%2 != 0):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
            if (i%2 == 0 and nums[i]%2 == 0) or (i%2 != 0 and nums[i]%2 != 0):
                i += 1
            elif (j%2 == 0 and nums[j]%2 == 0) or (j%2 != 0 and nums[j]%2 != 0):
                j -= 1
        return nums