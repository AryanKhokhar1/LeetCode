class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s) -1
        lis = list(s)
        while i < j:
            if lis[i] != lis[j]:
                if ord(lis[i]) < ord(lis[j]):
                    lis[j] = lis[i]
                else:
                    lis[i] = lis[j]
            i += 1
            j -= 1
        return "".join(lis)