class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        max_element = max(nums)
        ndigit = len(str(max_element))

        for i in range(ndigit):
            bucket = [[],[],[],[],[],[],[],[],[],[]]
            for ele in nums:
                focusdigit = (ele//(10**i))%10
                bucket[focusdigit].append(ele)
            
            new_lis = []
            for b in bucket:
                new_lis.extend(b)
            nums = new_lis
        
        max_diff = 0
        for i in range(1,len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i-1])
        return max_diff