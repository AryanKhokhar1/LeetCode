class ProductOfNumbers(object):
    
    def __init__(self):
        self.prefixProduct = []

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefixProduct = list()
        elif(len(self.prefixProduct) == 0):
            self.prefixProduct.append(num)
        else:
            self.prefixProduct.append(num*self.prefixProduct[-1])

        

    def getProduct(self, k):
        if len(self.prefixProduct) == k:
            return self.prefixProduct[-1]
        elif len(self.prefixProduct) > k:
            return self.prefixProduct[-1]/self.prefixProduct[-1-k]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)