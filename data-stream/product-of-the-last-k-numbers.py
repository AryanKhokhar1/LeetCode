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
        if k <= len(self.lis):
            mult = 1
            i = -1
            while( i >= ((-1)*k)):
                mult *= self.lis[i]
                i -= 1

            return mult


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)