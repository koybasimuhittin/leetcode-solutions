class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ans = len(nums)
        for i in range(len(nums)):
            if(nums [i] == target):
                ans = min(ans, abs(i - start))

        return ans