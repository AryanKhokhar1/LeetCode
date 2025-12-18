class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        mvalue = prices[0]
        for element in prices:
            if element > mvalue:
                mProfit = max(mProfit,element-mvalue)
            else:
                mvalue = element
        return mProfit