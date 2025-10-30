class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # first we will eliminate negatives
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        nums.sort()
        sum = 0
        if len(nums) %  2 == 0:
            maxi = nums[len(nums)//2:]
            mini = nums[:len(nums)//2]
            for i in range(len(maxi)):
                sum += maxi[i] ** 2
                sum -= mini[i] ** 2
        else:
            maxi = nums[len(nums)//2 :]
            mini = nums[:len(nums)//2 ]
            for i in range(len(mini)):
                sum += maxi[i] ** 2
                sum -= mini[i] ** 2
            sum += maxi[-1] ** 2
        return sum 
        
        