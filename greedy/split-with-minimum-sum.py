class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        lis = list()

        while(num != 0):
            lis.append(num%10)
            num = num//10
        lis.sort()

        num1 = ''
        num2 = ''
        i = 0
        for ele in lis:
            if(i%2 == 0):
                num1 += str(ele)
            else:
                num2 += str(ele)
            i += 1
        if(num1 == '' and num2 == ''):
            return 0
        elif(num1 == ""):
            return int(num2)
        elif(num2 == ""):
            return int(num1)
        else:
            return int(num1) + int(num2)