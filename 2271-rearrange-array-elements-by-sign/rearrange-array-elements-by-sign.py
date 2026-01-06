class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # with the help of two pointer approach
        i = 0
        j = 1
        ans = [0]*len(nums)
        for ele in nums:
            if ele > 0:
                ans[i] = ele
                i +=2
            elif ele < 0:
                ans[j] = ele
                j += 2
        return ans 
    