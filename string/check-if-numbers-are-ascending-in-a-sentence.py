class Solution(object):
    def areNumbersAscending(self, s):
        lis = s.split(" ")
        pre = -1
        for ele in lis:
            if ele.isdigit():

                if(pre >= int(ele)):
                    return False
                pre = int(ele)
        return True

        