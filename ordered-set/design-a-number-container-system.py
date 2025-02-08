class NumberContainers(object):

    def __init__(self):
        self.dic = dict()

    def change(self, index, number):
        self.dic[index] = number

        
    def find(self, number):
        for k,v in self.dic.items():
            if v == number:
                return k
        return -1
        
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)