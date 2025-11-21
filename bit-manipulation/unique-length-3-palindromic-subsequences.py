class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = set()
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                for k in range(j+1,len(s)):
                    curr_str = s[i]+s[j]+s[k]
                    if curr_str == curr_str[::-1]:
                        count.add(curr_str)
        return len(count)