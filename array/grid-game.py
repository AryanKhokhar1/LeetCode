class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        prefix = list()
        summ = 0
        for x in grid[0]:
            summ += x
            prefix.append(summ)
        
        bottom = 0
        answer = prefix[-1]
        for x in range(len(grid[1])):
            top = prefix[-1] - prefix[x]
            answer = min(answer, max(top, bottom))
            bottom += grid[1][x]
        return answer
        