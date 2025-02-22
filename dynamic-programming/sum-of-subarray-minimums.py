class Solution(object):
    def sumSubarrayMins(self, arr):
        summ = 0
        for i in range(1,len(arr)+1):
            n = 0
            while(i+n <= len(arr)):
                summ += min(arr[n:i+n])
                n+=1
        return summ