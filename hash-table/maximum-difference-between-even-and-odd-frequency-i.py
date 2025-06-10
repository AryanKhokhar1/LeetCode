class Solution(object):
    def maxDifference(self, s):
        maxoddfreq = 0
        maxevenfreq = 0
        frequency = dict()
        for ele in s:
            if frequency.get(ele) == None:
                frequency[ele] = 1
            else:
                frequency[ele] = frequency.get(ele) + 1
        
        for val in frequency.values():
            if val % 2 == 0:
                maxevenfreq = max(maxevenfreq, val)
            else:
                maxoddfreq = max(maxoddfreq, val)
        return (maxoddfreq - maxevenfreq)