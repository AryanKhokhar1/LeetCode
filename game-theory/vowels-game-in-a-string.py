class Solution(object):
    def doesAliceWin(self, s):
        if 'a'  in s  or 'e' in s or 'i' in s or 'o' in s or 'u' in s:
            return True
        else:
            return False
        