class Solution(object):
    def minimumRecolors(self, blocks, k):
        if k == len(blocks):
            return blocks.count("W")
        ans = blocks[:k].count("W")
        first = 0
        tempans = ans
        for i in range(k,len(blocks)):
            if blocks[first] == "W":
                tempans -= 1
            if blocks[i] == "W":
                tempans += 1
            first += 1
            ans = min(ans, tempans)
        return ans