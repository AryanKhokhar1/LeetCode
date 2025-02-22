class RecentCounter(object):

    def __init__(self):
        self.lis = list()
        self.curr_left_limit = 1

    def ping(self, t):
        self.lis.append(t)
        if t > 3000:
            self.curr_left_limit = t - 3000

        while self.curr_left_limit > self.lis[0]:
            self.lis.pop(0)
        return len(self.lis)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)