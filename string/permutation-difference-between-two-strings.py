class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        l = len(s)
        value  = 0
        for i in range(l):
            letter_from_s = s[i]
            for j in range(l):
                if(letter_from_s == t[j]):
                    if((i-j) <0):
                        value += (-1*(i-j))
                    else:
                        value += (i-j)
                    

        return value