class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        else:
            lis = [True]*(n)
        
        lis[0] = lis[1] = False
        for ind in range(2,int(n**0.5)+1):
            if lis[ind]:
                for i in range(ind*2, n, ind):
                    lis[i] = False
        return sum(lis)