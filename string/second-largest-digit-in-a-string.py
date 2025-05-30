class Solution(object):
    def secondHighest(self, s):
        tempset = set()
        for i in range(len(s)):
            if(s[i].isdigit()):
                tempset.add(int(s[i]))
        if len(tempset) < 2:
            return -1
        lis = list(tempset)
        lis.sort()
        return lis[-2]