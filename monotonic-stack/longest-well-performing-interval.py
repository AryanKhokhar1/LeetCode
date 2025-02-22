class Solution(object):
    def longestWPI(self, hours):
        prefixsum1 = []
        prefixsum2 = []
        
        a , b = 0 , 0
        for i in range(len(hours)):
            if(hours[i] > 8):
                a += 1
            else:
                a -= 1

            if(hours[len(hours)-i-1] > 8):
                b += 1
            else:
                b -= 1
            prefixsum1.append(a)
            prefixsum2.insert(len(hours)-i-1,b)
        
        a = 0
        b = 0
        ansA = 0
        ansB = 0
        for ele in prefixsum1:
            if ele > 0:
                a += 1
            else:
                a = 0
            ansA = max(a,ansA)
        
        for ele in prefixsum2:
            if ele >0:
                b += 1
            else:
                b = 0
            ansB = max(b,ansB)
        return max(ansA,ansB)