class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        repeatednum = 0
        d = dict()
        summ = 0
        for sublis in grid:
            for ele in sublis:
                if d.get(ele) is None:
                    d[ele] = 1
                    summ += ele
                else:
                    repeatednum = ele
        l = len(grid)*len(grid[0])
        missingnum = ((l+1)*l)//2 - summ
        return [repeatednum, missingnum]
                    

