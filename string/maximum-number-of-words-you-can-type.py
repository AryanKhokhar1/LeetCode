class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        textlist = text.split(" ")
        answer = 0
        for word in textlist:
            inWord = True
            for i in range(len(brokenLetters)):
                if brokenLetters[i] in word:
                    inWord = False
                    break
            if inWord:
                answer += 1
        return answer