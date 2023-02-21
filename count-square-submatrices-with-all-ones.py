class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])
        add = min(n, m)
        ans = 0

        rowSum = [[0] for i in range(n)]
        columnSum = [[0] for i in range(m)]

        def isValid(x, y):
            return x < n and y < m


        for i in range(n):
            for j in range(m):
                rowSum[i].append(rowSum[i][-1] + matrix[i][j])
                columnSum[j].append(columnSum[j][-1] + matrix[i][j])

        for i in range(n):
            for j in range(m):
                sum = 0
                for k in range(add):
                    if isValid(i + k, j + k):
                        sum += columnSum[j + k][i + k + 1] + rowSum[i + k][j + k + 1] - columnSum[j + k][i] - rowSum[i + k][j] - 1
                        if(sum == (k + 1) * (k + 1)):
                            ans += 1
                        else:
                            break
                    else:
                        break

        return ans