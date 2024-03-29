class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        ans = 0
        sum2 = {}

        for i in nums3:
            for j in nums4:
                sum2[i + j] = sum2.get(i + j, 0) + 1

        for i in nums1:
            for j in nums2:
                ans += sum2.get(0 - i - j, 0)
        return ans