class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = sys.maxint

    def push(self, val):
        self.stack.append(val)   
        self.minimum = min(val, self.minimum)  

    def pop(self):
        if len(self.stack) > 0:
            val = self.stack.pop()
            
            if val == self.minimum and len(self.stack) > 0:
                self.minimum = min(self.stack)
            if len(self.stack) == 0:
                self.minimum = sys.maxint
            

    def top(self):
        if len(self.stack) < 1:
            return -1
        return self.stack[-1]

    def getMin(self):
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()