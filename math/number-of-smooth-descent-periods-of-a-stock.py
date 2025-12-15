class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        subarr = []
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                subarr.append(prices[i:j+1])
        answer = 0
        for sublis in subarr:
            if len(sublis) <= 1:
                answer +=1
            else:
                isdesc = True
                for i in range(1,len(sublis)):
                    if sublis[i-1] - sublis[i] != 1:
                        isdesc = False
                        break
                if isdesc:
                    answer += 1
        return answer