class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        neg = []
        pos = []
        for x in nums:
            if x < 0:
                neg.append(-x)
            else:
                pos.append(x)
        if neg:
            neg = self.countingsort(neg)
        if pos:
            pos = self.countingsort(pos)
        if neg:
            neg = list(reversed(neg))
            for i in range(len(neg)):
                neg[i] = -neg[i]
        sorted_lis = neg+pos
        ans = 0
        for i in range(1,len(sorted_lis),2):
            ans += min(sorted_lis[i],sorted_lis[i-1])
        return ans
            

    def countingsort(self,nums):
        maximum_element = max(nums)
        lis = [0]*(maximum_element+1)
        # [0,1,1,1,1] 0,1,2,3,4
        for ele in nums:
            lis[ele] += 1
        sorted_lis = [0]*len(nums)
        for i in range(1,len(lis)):
            lis[i] += lis[i-1]
        for ele in nums:
            lis[ele] -= 1
            sorted_lis[lis[ele]] = ele
        
        return sorted_lis