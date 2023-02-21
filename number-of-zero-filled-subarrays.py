class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = 0
        ans = 0

        for i in nums:
            if(i != 0):
                if(cnt != 0):
                    ans += (cnt * (cnt + 1)) // 2
                cnt = 0
            else:
                cnt += 1
        if(cnt != 0):
            ans += (cnt * (cnt + 1)) // 2

        return ans
