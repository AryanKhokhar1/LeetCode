class Solution(object):
    def encode(self, prev):
        newNum = ""
        count = 1
        for i in range(1,len(prev)):
            if prev[i-1] != prev[i]:
                newNum += (str(count) + str(prev[i-1]))
                count = 1
            else:
                count += 1
        newNum += (str(count) + str(prev[-1]))
        return newNum
    def countAndSay(self, n):
        ans = "1"
        for i in range(1,n):
            ans = self.encode(ans)
        return ans
            