class Solution(object):
    def subsetsWithDup(self, nums):
        answer = []
        nums.sort()
        def backtrack(curr, i):
            if i == len(nums):
                answer.append(curr[:])
                return
            
            curr.append(nums[i])
            backtrack(curr, i+1)

            curr.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(curr,i+1)

        backtrack([], 0)
        return answer