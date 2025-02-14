class Solution(object):
    def removeWhiteSpace(self, s):
        if(len(s) == 0 or (len(s)>0 and s[0] != ' ')):
            return self.positiveornegative(s)
        return self.removeWhiteSpace(s[1:])

    def positiveornegative(self,s):
        if len(s) > 0:
            if s[0] == '-':
                s = s[1:]
                self.signature = '-'
            elif s[0] == '+':
                s = s[1:]
                self.signature = '+'
            else:
                self.signature = '+'
        return self.number(s,0,0)
    
    def number(self,s,num,i):
        if i == len(s) or (ord(s[i]) <48 or ord(s[i]) >57):
            return self.checkInRange(num)
        num = (10 *num) + int(s[i])
        return self.number(s,num,i+1)
    def checkInRange(self,num):
        if self.signature == '-':
            num = -num
        return max(-2147483648, min(2147483647, num))
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.removeWhiteSpace(s)