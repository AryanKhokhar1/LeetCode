class Solution(object):
    def punishmentNumber(self, n):
        self.answer = 0
        for i in range(1,n+1):
            num = i**2
            self.isPunishable(i,str(num),0,0)
        return self.answer

    def isPunishable(self, n, num, curr, start):
        if start >= len(num):
            if n == curr:
                self.answer += int(num)
            return
        for i in range(start,len(num)):
            val = int(num[start:i+1])

            self.isPunishable(n, num, curr+val,i+1)

