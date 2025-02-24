class Solution(object):
    def sortSentence(self, s):
        lis = s.split(" ")
        answer = [0] * len(lis)

        for ele in lis:
            answer[int(ele[-1])-1] = ele[:-1]

        return ' '.join(answer)