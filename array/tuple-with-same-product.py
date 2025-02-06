class Solution(object):
    def tupleSameProduct(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """
        summ = dict()
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]

                if summ.get(product) == None:
                    summ[product] = 1
                else:
                    summ[product] += 1
        ans = 0
        for v in summ.values():
            if v > 1:
                ans += (v * (v-1))//2
        
        return 8*ans