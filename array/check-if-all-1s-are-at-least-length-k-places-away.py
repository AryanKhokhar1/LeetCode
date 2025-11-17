class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        answer = len(nums)
        start = -1
        diff = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if start == -1:
                    start = i
                else:
                    answer = min(answer,start)
                    start = 0
            else:
                start += 1
        if answer >= k:
            return True
        else:
            return False
