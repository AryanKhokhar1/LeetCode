class Solution:
    def removeZeros(self, n: int) -> int:
        ans = 0
        t = 0
        while(n>0):
            if n % 10 > 0:
                ans = (n%10) * (10**t) + ans
                t += 1
            n = n//10
        return ans