class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        indexOfS = 0
        indexOfT = 0

        while(indexOfT < len(t) and indexOfS < len(s)):
            if(s[indexOfS] == t[indexOfT]):
                indexOfS += 1
                indexOfT += 1
            else:
                indexOfT += 1

        return indexOfS == len(s)