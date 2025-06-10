class Solution(object):
    def maxDifference(self, s):
        maxoddfreq = 0
        maxevenfreq = 0
        minevenfreq = sys.maxint
        frequency = dict()
        for ele in s:
            if frequency.get(ele) == None:
                frequency[ele] = 1
            else:
                frequency[ele] = frequency.get(ele) + 1
        
        for val in frequency.values():
            if val % 2 == 0:
                maxevenfreq = max(maxevenfreq, val)
                minevenfreq = min(minevenfreq, val)
            else:
                maxoddfreq = max(maxoddfreq, val)
        if (maxoddfreq - maxevenfreq) < (maxoddfreq - minevenfreq):
            return maxoddfreq - minevenfreq
        else:
            return (maxoddfreq - maxevenfreq)