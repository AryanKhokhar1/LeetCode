class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        fnum = ''
        for i in range(len(number)):
            if(number[i] != '-' and number[i] != ' '):
                fnum += number[i]
        ansnum = ''
        i = 0
        while(len(fnum) != 0):
            if(len(fnum)>4):
                ansnum += fnum[:3]
                ansnum += "-"
                fnum = fnum[3:]
            elif(len(fnum) == 4):
                ansnum += fnum[:2]
                ansnum += "-"
                ansnum += fnum[2:4]
                fnum = fnum[4:]
            elif(len(fnum) == 3):
                ansnum += fnum[:3]
                fnum = fnum[3:]
            elif(len(fnum) == 2):
                ansnum += fnum[:2]
                fnum = fnum[2:]

        return ansnum