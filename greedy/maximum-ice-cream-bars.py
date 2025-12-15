class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_element = max(costs)+1
        count = [0]*max_element
        
        for ele in costs:
            count[ele] += 1
        print(count)
        for i in range(1, len(count)):
            count[i] += count[i-1]
        lis = [0] * len(costs)
        for ele in costs:
            lis[count[ele]-1] = ele
            count[ele]  -= 1
        
        total = 0
        for i in range(len(lis)):
            total += lis[i]
            if total > coins:
                return i
        return len(lis)