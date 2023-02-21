class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        increasing = False
        decreasing = False
        for i in range(1, len(nums)):
            if(nums[i] > nums[i - 1]):
                increasing = True
            elif(nums[i] < nums[i - 1]):
                decreasing = True

        if(increasing and decreasing):
            return False
        return True