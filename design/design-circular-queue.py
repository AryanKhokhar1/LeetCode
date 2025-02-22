class MyCircularQueue(object):

    def __init__(self, k):
        self.maxlen = k
        self.lis = []
        

    def enQueue(self, value):
        if not self.isFull():
            self.lis.append(value)
            return True
        return False
        

    def deQueue(self):
        if not self.isEmpty():
            self.lis.pop(0)
            return True
        return False
        

    def Front(self):
        if not self.isEmpty():
            return self.lis[0]
        return -1
        

    def Rear(self):
        if not self.isEmpty():
            return self.lis[-1]
        return -1
        

    def isEmpty(self):
        return len(self.lis) == 0
        

    def isFull(self):
        return len(self.lis) == self.maxlen
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()