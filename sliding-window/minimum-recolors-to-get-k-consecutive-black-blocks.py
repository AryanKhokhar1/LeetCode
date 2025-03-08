class Solution(object):
    def minimumRecolors(self, blocks, k):
        if k == len(blocks):
            return blocks.count("W")
        ans = k
        for i in range(k,len(blocks)):
            ans = min(ans, blocks.count("W",i-k,i+1))
        return ans
        