class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        s = ""
        mn = min(len(word1), len(word2))
        for i in range(mn):
            if i < len(word1):
                s += word1[i]
            if i < len(word2):
                s += word2[i]
        s += word1[mn:]
        s += word2[mn:]
        return s