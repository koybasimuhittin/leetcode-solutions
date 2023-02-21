class Solution(object):
    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        multipliersOfK = []

        def gcd(a, b):
            if(b == 0):
                return a
            return gcd(b, a % b)
        
        temp = []
        for i in nums:
            if(i % k != 0):
                if(len(temp) != 0):
                    multipliersOfK.append(temp)
                temp = []

            else:
                temp.append(i)
        multipliersOfK.append(temp)


        for i in multipliersOfK:
            for j in range(len(i)):
                arrGcd = k
                for m in range(j,len(i)):
                    if(j == m):
                        arrGcd = i[m]
                    else:
                        arrGcd = gcd(max(arrGcd, i[m]), min(arrGcd, i[m]))
                    if(arrGcd == k):
                        ans += 1
        return ans