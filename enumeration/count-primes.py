class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        else:
            lis = [True]*(n-1)
        
        for ind in range(2,len(lis)):
            if lis[ind]:
                i = ind
                i += i
                while(i<len(lis)):
                    lis[i] = False
                    i+=i
        answer = 0
        print(lis)
        for val in range(2,len(lis)):
            if lis[val]:
                answer += 1
        return answer