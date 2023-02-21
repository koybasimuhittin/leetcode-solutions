class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        cnt = 0
        for i in nums:
            if(i == 0):
                cnt = 0
            else:
                cnt += 1

            ans = max(ans, cnt)

        return ans