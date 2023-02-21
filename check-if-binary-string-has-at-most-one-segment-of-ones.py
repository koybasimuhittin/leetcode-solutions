class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """

        isOneSeen = False
        isZeroSeen = False

        for i in s:
            if(i == '0'and isOneSeen):
                isZeroSeen = True
            elif(i == '1' and isOneSeen and isZeroSeen):
                return False
            
            if(i == '1'):
                isOneSeen = True

        return True