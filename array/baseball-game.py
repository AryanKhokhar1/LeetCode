class Solution(object):
    def invalid(self):
        if(len(self.score) > 0):
            self.score.pop(-1)
    def double(self):
        if(len(self.score)>0):
            self.score.append(self.score[-1]*2)
    def addition(self):
        if(len(self.score) >1):
            self.score.append(self.score[-1]+self.score[-2])
    def calPoints(self, operations):
        self.score = []
        for op in operations:
            if op == "C":
                self.invalid()
            elif op == "D":
                self.double()
            elif op == "+":
                self.addition()
            else:
                self.score.append(int(op))
        s = 0
        for ele in self.score:
            s += ele
        return s