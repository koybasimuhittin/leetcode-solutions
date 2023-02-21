class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0]

        for i in nums:
            prevEven = dp[0]
            dp[0] = max(dp[0], dp[1] + i)
            dp[1] = max(dp[1], prevEven - i)

        return max(dp)