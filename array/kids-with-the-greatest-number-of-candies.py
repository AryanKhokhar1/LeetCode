class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        ans = []
        for ele in candies:
            if ele+extraCandies >= maximum:
                ans.append(True)
            else:
                ans.append(False)
        return ans