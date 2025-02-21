class Solution(object):
    def nextGreaterElements(self, nums):
        result = [-1]*len(nums)
        nums = nums*2
        stack = []
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]]< nums[i]:
                index = stack.pop()
                result[index] = nums[i]
            
            stack.append(i%len(result))
        return result