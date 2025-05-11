class Solution(object):
    def threeConsecutiveOdds(self, arr):
        num = 0
        for ele in arr:
            if ele%2 == 1:
                num += 1
            else:
                num = 0
            if num == 3:
                return True

        return False