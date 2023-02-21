class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        visited = [False for i in range(left, right + 1)]

        n = len(ranges)
        m = len(ranges[0])

        for i in ranges:
            for j in range(i[0], i[1] + 1):
                if(left <= j <= right):
                    visited[j - left] = True

        for i in visited:
            if(i == False):
                return False
        return True