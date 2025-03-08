class Solution(object):
    def minimumRecolors(self, blocks, k):
        if k == len(blocks):
            return blocks.count("W")
        ans = k
        for i in range(k,len(blocks)+1):
            ans = min(ans, blocks.count("W",i-k,i))
        return ans
        