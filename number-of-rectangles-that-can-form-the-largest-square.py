class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxLen = 0
        ans = 0
        for i in rectangles:
            maxLen = max(maxLen, min(i[0], i[1]))

        for i in rectangles:
            if(i[0] >= maxLen and i[1] >= maxLen):
                ans += 1
        
        return ans