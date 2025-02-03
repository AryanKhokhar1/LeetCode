class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        length = len(word)
        if length <= 8:
            return length
        elif length <= 16:
            return 8 + ((length - 8)*2)
        elif length <= 24:
            return 8 + 16 + ((length - 16)*3)
        else:
            return 8 + 16 + 24 + ((length - 24)*4)