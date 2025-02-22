class MyCircularDeque(object):

    def __init__(self, k):
        self.lis = list()
        self.maxlen = k
        

    def insertFront(self, value):
        if not self.isFull():
            self.lis.insert(0,value)
            return True
        return False
        

    def insertLast(self, value):
        if not self.isFull():
            self.lis.append(value)
            return True
        return False
        

    def deleteFront(self):
        if not self.isEmpty():
            self.lis.pop(0)
            return True
        
        return False

    def deleteLast(self):
        if not self.isEmpty():
            self.lis.pop()
            return True
        return False
        

    def getFront(self):
        if not self.isEmpty():
            return self.lis[0]
        return -1
        

    def getRear(self):
        if not self.isEmpty():
            return self.lis[-1]
        return -1
        

    def isEmpty(self):
        return len(self.lis) == 0
        

    def isFull(self):
        return len(self.lis) == self.maxlen
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()