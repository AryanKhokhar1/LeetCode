class Solution(object):
    def divideString(self, s, k, fill):
        if not s:
            return []
        n = len(s)//k
        lis = []
        for i in range(n):
            lis.append(s[(k*i):(k*i+k)])
        if len(s)%k != 0:
            word = s[n*k:]
            extranum = k - len(word)
            word += extranum * fill
            lis.append(word)
        return lis