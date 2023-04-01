class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = a[::-1]  # reverse the binary string
        b = b[::-1]  # reverse the binary string

        ## make the binary strings equal in length with adding zeroes ##
        while (len(a) < len(b)):
            a += "0"

        while (len(b) < len(a)):
            b += "0"

        ## binary sum ##
        addition = 0  # if the sum exceeds to next digit
        answer = ""

        for index in range(len(a)):
            # sum = addition + a[index] + b[index]
            digitA = int(a[index])
            digitB = int(b[index])
            sum = digitA + digitB + addition

            '''
                if a == 1 && b == 1 current is 0 add 1 to next and current = 0
                if a == 1 && b == 0
                    if addition is 0 add 1 to current go to next
                    if addition is 1 current = 0 add 1 to next
                if a == 0 && b == 0
                    add adition to current
            '''

            answer += str(sum % 2)
            if (sum > 1):
                addition = 1
            else:
                addition = 0

        if (addition == 1):
            answer += '1'

        answer = answer[::-1]
        return answer
