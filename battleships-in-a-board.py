class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        n = len(board)
        m = len(board[0])
        cnt = 0

        visited = [[False for i in range(m)] for j in range(n)]
        
        def isValidCordinate(x, y):
            return (x < m and y < n and x >= 0 and y >= 0)

        def traverse(x, y):
            if(not(isValidCordinate(x, y)) or visited[y][x] or board[y][x] == '.'):
                return

            visited[y][x] = True
            points = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for point in points:
                traverse(x + point[0], y + point[1])

        for i in range(n):
            for j in range(m):
                if(board[i][j] == 'X' and visited[i][j] != True):
                    traverse(j, i)
                    cnt += 1

        return cnt
