class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])
        visited = [[False for i in range(m)] for j in range(n)]

        def isValid(x, y):
            return x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 1

        def traverse(x, y):
            visited[x][y] = True
            ans = 0
            for i in [-1, 1]:
                if isValid(x + i, y) and not(visited[x + i][y]):
                    ans += traverse(x + i, y) + 1
                if isValid(x, y + i) and not(visited[x][y + i]):
                    ans += traverse(x, y + i) + 1
            return ans
        ans = 0  
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1 and not(visited[i][j])):
                    ans = max(ans, traverse(i, j) + 1)

        return ans