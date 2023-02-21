class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        intNums = []
        for i in nums:
            intNums.append(int(i))
        
        intNums.sort()
        return str(intNums[-k])