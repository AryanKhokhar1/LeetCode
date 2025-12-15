class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        z = 0
        addition = 0
        while(n > 0):
            r = n%10 
            if r != 0:
                addition += r
                x = r*(10**z) + x
                z += 1
            n = n//10
        return x*addition