class Solution(object):
    def secondHighest(self, s):
        a = None
        b = None
        for i in range(len(s)):
            if(s[i].isdigit()):
                if a == None:
                    a = int(s[i])
                elif a < int(s[i]):
                    b = a
                    a = int(s[i])
                elif a > int(s[i]) and a != int(s[i]) and ( b == None or int(s[i]) > b):
                    b = int(s[i])
        if b == None:
            return -1
        return b