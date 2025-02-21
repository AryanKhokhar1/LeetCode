class Solution(object):
    def backspaceCompare(self, s, t):
        stack1 = list(s)
        stack2 = list(t)
        str1 = ""
        str2 = ""
        i = len(stack1) -1
        skip = 0
        while i >= 0:
            val = stack1.pop()
            if val == "#":
                skip += 1
            else:
                if skip:
                    skip -= 1
                else:
                    str1 = val + str1
            i -= 1
        skip = 0
        i = len(stack2) -1
        while i >= 0:
            val = stack2.pop()
            if val == "#":
                skip += 1
            else:
                if not skip:
                    str2 = val + str2
                else:
                    skip -= 1
            i -= 1
        print(str1, str2)
        return str1 == str2