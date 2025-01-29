class Solution(object):

    def sqrt(self, min, max ,num):
        print(min,max,num)
        if(max - min <= 1):
            return min
        half = (max+min)//2
        if(half**2 == num):
            return half
        elif(half**2 < num):
            return self.sqrt(half, max, num)
        elif(half**2 > num):
            return self.sqrt(min,half,num)
    def mySqrt(self, x):
        if x == 1 or x == 0:
            return x
        return self.sqrt(0,x,x)
        