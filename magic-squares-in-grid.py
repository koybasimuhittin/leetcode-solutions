class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0

        def checkIsMagic(arr):
            rowSum = [0, 0, 0]
            columnSum = [0, 0, 0]
            diagonalSum = [0, 0]
            visited = [False for i in range(10)]
            visited[0] = True

            for i in range(3):
                for j in range(3):
                    if(arr[i][j] > 9 or arr[i][j] < 1):
                        return False
                    visited[arr[i][j]] = True
                    rowSum[i] += arr[i][j]
                    columnSum[j] += arr[i][j]

                    if(i == j):
                        diagonalSum[0] += arr[i][j]
                        if(i == 1):
                            diagonalSum[1] += arr[i][j]
                    elif((i == 0 and j == 2) or (i == 2 and j == 0)):
                        diagonalSum[1] += arr[i][j]

            if(False in visited):
                return False
            
            for i in range(3):
                if(rowSum[i] != 15 or columnSum[i] != 15):
                    return False
            if(diagonalSum[0] != 15 or diagonalSum[1] != 15):
                return False
            
            return True

        n = len(grid)
        m = len(grid[0])

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                temp = []
                for k in range(i - 1, i + 2):
                    ttemp = []
                    for l in range (j - 1, j + 2):
                        ttemp.append(grid[k][l])
                    temp.append(ttemp)
                if(checkIsMagic(temp)):
                    ans += 1
        return ans