class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        newMatrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                newMatrix[j][i] = matrix[i][j]

        return newMatrix