class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        prev = 0
        for x in range(len(s)):
            t = t[prev:]
            if(s[x] in t):
                prev = t.index(s[x]) +1
            else:
                return False
        return True
        