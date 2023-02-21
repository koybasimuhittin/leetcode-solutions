class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        odds = []
        evens = []
        arr = []
        while(num > 0):
            if((num % 10) % 2 == 1):
                odds.append(num % 10)
                arr.append(True)
            else:
                evens.append(num % 10)
                arr.append(False)
            num /= 10
        odds.sort()
        odds.reverse()
        evens.sort()
        evens.reverse()
        print(odds, evens)
        i = 0
        j = 0
        ans = ""
        for k in arr[::-1]:
            if(k):
                ans += (str(odds[i]))
                i += 1
            else:
                ans += (str(evens[j]))
                j += 1

        return int(ans)
