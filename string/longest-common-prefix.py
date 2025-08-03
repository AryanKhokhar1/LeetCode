class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        same = strs[0]
        for ele in strs[1:]:
            for i in range(min(len(ele),len(same))):
                if ele[i] != same[i]:
                    same = same[:i]
                    break
        return same
