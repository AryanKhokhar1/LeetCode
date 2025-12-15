class Solution:
    def minimumFlips(self, n: int) -> int:
        s = format(n,'b')
        rs = s[::-1]
        count = 0
        for i in range(len(s)):
            if s[i] != rs[i]:
                count += 1
        return count