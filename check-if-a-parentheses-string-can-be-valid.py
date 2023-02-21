class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """

        if(len(s) % 2 == 1):
            return False
        
        else:
            counter = 0
            for i in range(len(s)):
                if(s[i] == ')' and locked[i] == '1'):
                    counter += 1
                if(counter * 2 > i + 1):
                    return False
            counter = 0
            for i in range(len(s)):
                if(s[len(s) - i - 1] == '(' and locked[len(s) - i - 1] == '1'):
                    counter += 1
                if(counter * 2 > i + 1):
                    return False

        return True
        