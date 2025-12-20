class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if (nums[i]%2 == 0 and i%2!=0) or (nums[i]%2 != 0 and i%2 == 0):
                isEven = bool(i%2 == 0)
                for j in range(i+1,len(nums)):
                    if isEven:
                        if nums[j]%2 == 0:
                            nums[i],nums[j] = nums[j],nums[i]
                            break
                    else:
                        if nums[j]%2 != 0:
                            nums[i],nums[j] = nums[j],nums[i]
                            break
        return nums