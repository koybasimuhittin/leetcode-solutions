class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        cnt = 0

        while(n >= 7):
            ans += 28 + 7 * cnt
            cnt += 1
            n -= 7
        
        ans += n * cnt + (n * (n + 1)) // 2
    
        return ans