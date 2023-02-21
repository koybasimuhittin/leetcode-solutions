class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = max(nums)
        r = sum(nums)

        def isValid(maxTotal):
            cnt = 1
            sum = 0
            for i in nums:
                sum += i
                if(sum > maxTotal):
                    sum = i
                    cnt += 1
            if(sum > maxTotal):
                cnt += 1
            return cnt <= k

        ans = r
        while(l < r):
            mid = l + (r - l) / 2
            if(isValid(mid)):
                ans = min(ans, mid)
                r = mid
            else:
                l = mid + 1
        
        return ans
