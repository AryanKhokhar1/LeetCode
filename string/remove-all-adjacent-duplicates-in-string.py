class Solution(object):
    def removeDuplicates(self, s):
        stack = [""]
        for i in s:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)