class Solution(object):
    def removeDuplicates(self, s):
        stack = list()
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
        return "".join(stack)