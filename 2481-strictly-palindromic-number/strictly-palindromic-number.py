class Solution:
    def baseval(self ,num ,base):
        ans = ""
        while num != 0:
            rem = num % base
            num = num // base
            ans = str(rem) + ans
        return ans
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            # get all base representation
            base_representation = self.baseval(n,i)
            if base_representation != base_representation[::-1]:
                return False
        return True