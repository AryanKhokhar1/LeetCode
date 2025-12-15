class Solution:
    def numSub(self, s: str) -> int:
        lis = []
        mod = 10**9 + 7
        sub = 0
        for i in range(len(s)):
            if s[i] == "1":
                sub += 1
            else:
                if sub > 0:
                    lis.append(sub)
                    sub = 0
        if sub > 0:
            lis.append(sub)
        answer = 0
        for n in lis:
            answer += n * (n+1)//2 % mod
        return answer
                
