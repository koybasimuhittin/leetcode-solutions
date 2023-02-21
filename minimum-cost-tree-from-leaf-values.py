class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """


        def getMaxIdx(arr):
            maxi = 0
            maxIdx = -1
            for i in range(len(arr)):
                if(arr[i] > maxi):
                    maxi = arr[i]
                    maxIdx = i

            return (maxi, maxIdx)

        def calculateAll(arr):
            print(arr)
            if(len(arr) == 1):
                return (0, arr[0])

            maxi = getMaxIdx(arr)
            maxL = getMaxIdx(arr[: maxi[1]])
            maxR = getMaxIdx(arr[maxi[1] + 1 :])
            if(maxL[0] < maxR[0]):
                left = calculateAll(arr[: maxi[1] + 1])
                right = calculateAll(arr[maxi[1] + 1 :])
                return (left[0] + right[0] + left[1] * right[1], max(left[1], right[1]))
            else:
                left = calculateAll(arr[: maxi[1]])
                right = calculateAll(arr[maxi[1] :])
                return (left[0] + right[0] + left[1] * right[1], max(left[1], right[1]))

        return calculateAll(arr)[0]