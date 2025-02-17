class Solution(object):
    def numTilePossibilities(self, tiles):
        count = Counter(tiles)
        
        def backtrack():
            res = 0
            for ch in count:
                if count[ch] > 0:
                    res += 1
                    count[ch] -= 1
                    res += backtrack()
                    count[ch] += 1
            return res
        return backtrack()
                
