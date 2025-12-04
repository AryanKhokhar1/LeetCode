class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        ans = sys.maxsize
        while j <= len(nums):
            sub = nums[i:j]
            bor = -1
            if len(sub) == 0:
                bor = -1
            else:
                bor = 0
                for ele in sub:
                    bor |= ele

            if bor < k:
                j += 1
            else:
                ans = min(ans,j-i)
                if i ==j:
                    i+= 1
                    j+= 1
                else:
                    i+=1
        return -1 if ans == sys.maxsize else ans
                

                