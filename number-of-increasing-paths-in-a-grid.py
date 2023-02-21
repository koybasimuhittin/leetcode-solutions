class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mod = 1000000007
        n = len(grid)
        m = len(grid[0])

        dp = [[-1 for j in range(m)] for k in range(n)]
        
        def calc(x, y):
            if(x >= n or y >= m or x < 0 or y < 0):
                return 0
            if(dp[x][y] != -1):
                return dp[x][y]
            ans = 1
            if(x-1 >= 0 and grid[x-1][y] > grid[x][y]):
                ans += calc(x-1, y) % mod
                ans %= mod
            if(x+1 < n and grid[x+1][y] > grid[x][y]):
                ans += calc(x+1, y) % mod
                ans %= mod
            if(y-1 >= 0 and grid[x][y-1] > grid[x][y]):
                ans += calc(x, y-1) % mod
                ans %= mod
            if(y+1 < m and grid[x][y+1] > grid[x][y]):
                ans += calc(x, y+1) % mod
                ans %= mod

            dp[x][y] = ans % mod
            return ans % mod

        for x in range(n):
            for y in range(m):
                if(dp[x][y] == -1):
                    calc(x, y)
        ans = 0
        for i in range(n):
            for j in range(m):
                ans += dp[i][j] % mod
                ans %= mod
        
        return ans