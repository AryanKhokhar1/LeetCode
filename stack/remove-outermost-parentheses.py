class Solution(object):
    def removeOuterParentheses(self, s):
        isBalance = 0
        stack = list()
        ans = ''
        for i in range(len(s)):
            if isBalance == 0 and s[i] == "(": #First
                isBalance += 1
            elif isBalance == 1 and s[i] == ")": #Last
                isBalance -=1
            else:
                if s[i] == "(":
                    isBalance += 1
                    ans = ans + s[i]
                else:
                    isBalance -= 1
                    ans = ans + s[i]
        return ans