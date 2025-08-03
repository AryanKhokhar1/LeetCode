class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        same = strs[0]
        for ele in strs[1:]:
            print(same, ", ", ele)
            print(type(same),type(ele))
            print(min(len(ele),len(same)))
            for i in range(min(len(ele),len(same))):
                print(i)
                if ele[i] != same[i]:
                    same = same[:i]
                    break
                elif i == len(ele) -1:
                    same = same[:i+1]
            print("same = ",same)
        return same
