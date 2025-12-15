class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        maximum_height = max(heights)
        count = [0]*(maximum_height+1)
        for ele in heights:
            count[ele] += 1
        
        for i in range(1,len(count)):
            count[i] += count[i-1]
        
        sorted_lis = [0]*len(heights)
        for ele in heights:
            count[ele] -= 1
            sorted_lis[count[ele]] = ele
        
        ans = 0
        for i in range(len(sorted_lis)):
            if heights[i] != sorted_lis[i]:
                ans +=  1
        return ans