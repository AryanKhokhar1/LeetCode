class ProductOfNumbers(object):
    
    def __init__(self):
        self.lis  = list()

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.lis.append(num)
        

    def getProduct(self, k):
        if k < len(self.lis):
            mult = 1
            for i in range(len(self.lis)-1,len(self.lis)-k-1,-1):
                mult *= self.lis[i]
            return mult


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)