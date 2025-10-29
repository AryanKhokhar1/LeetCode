class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = ""
        while(n != 0):
            binary = str(n %2) + binary 
            n = n // 2
        l = len(binary)
        answer = 0
        for i in range(l):
            answer += 2 ** i
        return answer 