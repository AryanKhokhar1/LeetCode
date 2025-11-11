class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        uniqueChar = set(s)
        for ele in uniqueChar:
            if s.count(ele) != t.count(ele):
                return False
        return True