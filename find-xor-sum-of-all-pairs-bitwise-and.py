class Solution(object):
    def getXORSum(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        ans = 0
        counterOfOnes = [[0 for i in range(30)] for j in range(2)]
        for i in arr1:
            cnt = 1
            for j in range(30):
                counterOfOnes[0][j] += (i & cnt) > 0
                cnt = cnt << 1
        for i in arr2:
            cnt = 1
            for j in range(30):
                counterOfOnes[1][j] += (i & cnt) > 0
                cnt = cnt << 1
        cnt = 1
        for i in range(30):
            if((counterOfOnes[0][i] * counterOfOnes[1][i]) % 2 == 1):
                ans += cnt
            cnt = cnt << 1
        return ans