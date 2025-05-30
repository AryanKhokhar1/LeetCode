class Solution(object):
    def secondHighest(self, s):
        a = None
        b = None
        for i in range(len(s)):
            if(s[i].isdigit()):
                num = int(s[i])
                if a == None:
                    a = num
                elif a < num:
                    b = a
                    a = num
                elif a > num and a != num and ( b == None or num > b):
                    b = num
        if b == None:
            return -1
        return b