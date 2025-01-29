class Solution(object):
    def rright(self, string):
        if(len(string) == 0 or string[-1].isalpha()):
            return string
            
        return self.rright(string[:-1])

    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        words = s.split(" ")
        biggest_word = max(len(word) for word in words)
        
        answer = list()
        for i in range(biggest_word):
            verticalword = ""
            for j in words:
                if(len(j)>i):
                    verticalword += j[i]
                else:
                    verticalword += " "
            
            answer.append(self.rright(verticalword))
        return answer


        