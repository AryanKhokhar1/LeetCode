class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # with help of extra array
        arr = [0]*len(nums)
        i,j = 0,1
        for index in range(len(nums)):
            if nums[index] < 0:
                # negative
                arr[j] = nums[index]
                j += 2
            else:
                # positive
                arr[i] = nums[index]
                i +=2
        return arr