class Solution(object):
    def longestWPI(self, hours):
        result = [-1]*len(hours)
        for i in range(len(hours)):
            if hours[i] > 8:
                result[i] = 1
        
        curr = 0
        ans = 0
        count = 0
        for i in range(len(hours)):
            if hours[i] > 8:
                curr += 1
            else:
                if curr > 0:
                    curr -= 1
                else:
                    curr = 0
            
            if curr > 0:
                count+= 1
            else:
                count = 0

            ans = max(ans,count)
        return ans