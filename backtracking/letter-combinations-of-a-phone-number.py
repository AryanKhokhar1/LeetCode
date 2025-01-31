class Solution(object):
    def combination(self,pr, unpr ,digitChar):
        if(len(unpr) == 0):
            return pr
        
        ans = list()
        val = digitChar[unpr[0]]
        for i in val:
            ans.extend(p + i for p in pr)
        return self.combination(ans, unpr[1:],digitChar)
         
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        digitChar = {
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
        }
        return self.combination([''],digits,digitChar)