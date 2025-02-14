class Solution(object):
    def ispalindrome(self,st):
        return st == st[::-1]
    def partition(self, s):
        
        result = []
        partition = []

        def dfs(i):
            if i>= len(s):
                result.append(partition[:])
                return
            
            for j in range(i,len(s)):
                if(self.ispalindrome(s[i:j+1])):
                    partition.append(s[i:j+1])

                    dfs(j+1)

                    partition.pop()
        dfs(0)
        return result
        