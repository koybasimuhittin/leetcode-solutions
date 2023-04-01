# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        answer = ListNode()
        ansTail = answer
        ansTailBack = ansTail

        addition = 0

        while (l1 != None and l2 != None):
            sum = addition + l1.val + l2.val
            addition = sum // 10
            l1 = l1.next
            l2 = l2.next

            ansTailBack = ansTail
            ansTail.val = sum % 10
            ansTail.next = ListNode()
            ansTail = ansTail.next

        while (l1 != None):
            sum = addition + l1.val
            addition = sum // 10
            l1 = l1.next

            ansTailBack = ansTail
            ansTail.val = sum % 10
            ansTail.next = ListNode()
            ansTail = ansTail.next

        while (l2 != None):
            sum = addition + l2.val
            addition = sum // 10
            l2 = l2.next

            ansTailBack = ansTail
            ansTail.val = sum % 10
            ansTail.next = ListNode()
            ansTail = ansTail.next

        if (addition > 0):
            ansTail.val = addition
        else:
            ansTailBack.next = None

        return answer
