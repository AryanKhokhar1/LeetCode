class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] == "a":
                a += 1
            else:
                b += 1
        if a > b:
            return a - b
        elif b > a:
            return b - a
        else: 
            return 0