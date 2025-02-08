class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        left = self.uniquePaths(m-1, n)
        right = self.uniquePaths(m,n-1)
        return left + right
        