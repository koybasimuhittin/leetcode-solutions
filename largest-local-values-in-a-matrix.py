class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        newGrid = [[0 for i in range(n - 2)] for j in range(n - 2)]

        def getMax(x, y):
            maxi = -1
            for i in [-1, 0 ,1]:
                for j in [-1, 0, 1]:
                    maxi = max(maxi, grid[x + i][y + j])
            return maxi

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                newGrid[i - 1][j - 1] = getMax(i , j)

        return newGrid