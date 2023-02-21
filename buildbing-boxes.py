class Solution(object):
    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = 0

        while(left < right):
            mid = left + (right - left) // 2
            if(((mid - 1) * mid * (mid + 1)) / 6 > n):
                right = mid 
            elif(((mid - 1) * mid * (mid + 1)) / 6 < n):
                left = mid + 1
            else:
                break
        mid = mid - 2
        while(((mid + 1) * (mid + 2) * (mid + 3)) // 6 <= n):
            mid+= 1
        
        floor = ((mid) * (mid + 1)) // 2
        boxLeft = n - (mid * (mid + 1) * (mid + 2)) // 6
        print(floor, boxLeft)
        if(boxLeft > 0):
            for i in range(1, mid + 2):
                if (i * (i + 1)) // 2 >= boxLeft:
                    floor += i
                    break

        return floor
        
        return mid
    