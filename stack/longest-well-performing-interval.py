class Solution(object):
    def longestWPI(self, hours):
        result = [1 if i >8 else -1 for i in hours]
        prefixSum = 0
        longest_interval = 0
        d = {}
        for i in range(len(hours)):
            prefixSum += result[i]

            if prefixSum > 0:
                longest_interval = i + 1
            else:
                if prefixSum -1 in d:
                    longest_interval = max(longest_interval, i-d[prefixSum -1])
            if prefixSum not in d:
                d[prefixSum] = i
        return longest_interval