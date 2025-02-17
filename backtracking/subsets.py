class Solution(object):
    def subsets(self, nums):
        answer = []
        def backtrack(curr,i):
            if i == len(nums):
                answer.append(curr[:])
                return

            curr.append(nums[i])
            backtrack(curr,i+1)
             
            curr.pop()

            backtrack(curr, i+1)

        backtrack([],0)
        return answer