class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for i in range(num1,num2+1):
            s = str(i)
            peaks = 0
            valleys = 0
            for a in range(1,len(s)-1):
                if s[a-1] < s[a] and s[a] > s[a+1]:
                    peaks += 1
                elif s[a] < s[a-1] and s[a] < s[a+1]:
                    valleys += 1
            waviness += peaks
            waviness += valleys
        return waviness
                