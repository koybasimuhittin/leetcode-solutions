class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """

        countDict = {}

        for c in s:
            countDict[c] = countDict.get(c, 0) + 1

        locationDict = {}
        count = 0
        ans = 0
        for i in range(0, len(s)):
            if(locationDict.get(s[i], False)):
                locationDict[s[i]].append(i)
                ans += count
            else:
                count += 1
                ans += count
                locationDict[s[i]] = [i]

        for key in locationDict:
            locationDict[key].append(len(s))

        tempAns = ans
        countDict = {s[0]:1}
      
        for i in range(1, len(s)):
            
            if(countDict.get(s[i - 1], 0) > 0):
                rightAfter = locationDict[s[i - 1]][countDict[s[i -1]]]
                tempAns -= len(s) - i + 1 - (len(s) - rightAfter)
            else:
                rightAfter = locationDict[s[i - 1]][0]
                tempAns -= len(s) - i + 1 - (len(s) - rightAfter)
            countDict[s[i]] = countDict.get(s[i], 0) + 1
            ans += tempAns
        return ans