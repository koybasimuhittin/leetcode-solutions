class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def isConnected(x, y, visit, grid, m):
            visit[x][y] = True
            if(grid[x][y] > m):
                return False

            if(x == len(grid) - 1 and y == len(grid) - 1):
                return True

            ans = False

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if(i != j and -2 < i - j  and i - j < 2 and x - i >= 0 and x - i <len(grid) and y - j >= 0 and y - j <len(grid) and not visit[x-i][y-j]):
                        print(x-i, y-j)
                        ans |= isConnected(x - i, y - j, visit, grid, m)
            return ans


        def checkConnected(grid, m):
            visit = [[False for i in range(len(grid))] for j in range(len(grid))]
            return isConnected(0, 0, visit, grid, m)

        r = len(grid) ** 2 - 1
        l = 0
        ans = r

        while(l <= r):
            m = l + (r - l) / 2
            if(checkConnected(grid, m)):
                print(m)
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans
