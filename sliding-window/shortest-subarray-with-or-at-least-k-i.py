class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1
        i = 0
        j = 0
        ans = 100
        while j <= len(nums):
            sub = nums[i:j]
            bor = 0
            if len(sub) == 0:
                bor = 0
            elif len(sub) == 1:
                bor = sub[0]
            else:
                bor = 0
                for ele in sub:
                    bor |= ele
            if bor < k:
                j += 1
            else:
                ans = min(ans,j-i)
                if i == j:
                    i+=1
                    j += 1
                else:
                    i+=1
                
        if ans == 100:
            return -1
        else:
            return ans

