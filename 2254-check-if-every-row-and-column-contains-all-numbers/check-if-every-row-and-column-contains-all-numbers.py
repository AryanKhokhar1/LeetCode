class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        setM = set()
        for i in range(1,len(matrix)+1):
            setM.add(i)
        for r in range(len(matrix)):
            if set(matrix[r]) != setM:
                return False
        for c in range(len(matrix)):
            tempset = set()
            for r in range(len(matrix)):
                tempset.add(matrix[r][c])
            if tempset != setM:
                return False
        return True