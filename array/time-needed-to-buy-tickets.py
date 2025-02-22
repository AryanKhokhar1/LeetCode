class Solution(object):
    def timeRequiredToBuy(self, tickets, k):

        # val = tickets[k]
        time = 0
        while tickets[k]:
            tickets[0] -= 1
            if(tickets[0] > 0):
                tickets.append(tickets.pop(0))
                time+= 1
                if k == 0:
                    k = len(tickets)-1
                else:
                    k -= 1
            else:
                tickets.pop(0)
                time += 1
                if k == 0:
                    break
                else:
                    k -= 1
        return time