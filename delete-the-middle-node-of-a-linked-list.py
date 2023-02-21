# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        before = head
        after = head
        cnt = 0
        size = 0
        tempHead = head
        while(tempHead != None):
            tempHead = tempHead.next
            size += 1
        tempHead = head
        if size == 1:
            return head.next
        while(cnt < size // 2):
            before = tempHead
            tempHead = tempHead.next
            after = tempHead.next
            cnt += 1
        before.next = after
        return head