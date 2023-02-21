class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dict = {}

        for i in arr:
            dict[i] = dict.get(i, 0) + 1

        cnt = 0
        for i in arr:
            if(dict[i] == 1):
                cnt += 1
                if(cnt == k):
                    return i
        return ""