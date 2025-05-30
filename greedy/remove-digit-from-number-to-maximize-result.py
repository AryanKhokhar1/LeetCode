class Solution(object):
    def removeDigit(self, number, digit):
        maxlis = -1
        for i in range(len(number)):
            if number[i] == digit:
                value = int(number[0:i] + number[i+1:])
                maxlis = max(value, maxlis)
        return str(maxlis)