class NumberContainers(object):

    def __init__(self):
        self.lis = list()

    def change(self, index, number):
        if len(self.lis) < index+1 :
            for i in range(index-(len(self.lis))):
                self.lis.append(None)
            self.lis.append(number)
        else:
            self.lis[index] = number

        
    def find(self, number):
        try:
            return self.lis.index(number)
        except:
            return -1
        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)