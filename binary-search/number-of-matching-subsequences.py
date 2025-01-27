class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        answer = 0
        for word in words:
            prev = 0
            temps = s
            for x in range(len(word)):
                temps = temps[prev:]
                if(word[x] in temps):
                    prev = temps.index(word[x]) + 1
                else:
                    if(answer > 0):
                        answer  -= 1
                        break
            answer += 1
        return answer