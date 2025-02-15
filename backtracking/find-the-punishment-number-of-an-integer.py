class Solution(object):
    def punishmentNumber(self, n):
        answer = 0
        for i in range(1,n+1):
            num = i**2
            if self.isPunishable(i,str(num),0,0):
                answer += num
        return answer

    def isPunishable(self, n, num, curr, start):
        if start >= len(num):
            return curr == n
        for i in range(start,len(num)):
            val = int(num[start:i+1])

            if self.isPunishable(n, num, curr+val,i+1):
                return True
        return False

