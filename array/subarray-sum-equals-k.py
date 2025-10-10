class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        d[0] = 1
        count = 0
        currsum = 0
        for ele in nums:
            currsum += ele

            if (currsum - k) in d:
                count += d[currsum -k]
            
            d[currsum] = d.get(currsum, 0) + 1
        return count