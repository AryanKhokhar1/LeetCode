import numpy as np
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        matrix = []
        for i in range(n):
            submatrix = []
            for j in range(n):
                submatrix.append(0)
            matrix.append(submatrix)
        
        for r1,c1,r2,c2 in queries:
            for r in range(r1,r2+1):
                for c in range(c1, c2+1):
                    matrix[r][c] += 1
        return matrix