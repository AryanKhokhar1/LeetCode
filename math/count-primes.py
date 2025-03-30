class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        else:
            lis = [True]*(n)
        
        lis[0] = lis[1] = False
        for ind in range(2,int(len(lis)**0.5)+1):
            if lis[ind]:
                i = ind
                i += ind
                while(i<len(lis)):
                    lis[i] = False
                    i+=ind
        return sum(lis)