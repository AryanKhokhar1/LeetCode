class Solution(object):
    def firstUniqChar(self, s):
        c = dict(Counter(s))
        for i in range(len(s)):
            if c.get(s[i]) == 1:
                return i
        return -1