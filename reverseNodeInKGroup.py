# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        length = 0
        traverse = head
        while traverse:
            length += 1
            traverse = traverse.next

        limit = length // k
        if k<= 1 or limit == 0:
            return head

        curr = head
        prev_tail = None
        new_head = None

        for i in range(limit):
            prev = None
            group_head = curr
            j = 0

            while j<k:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
                j += 1

            if not new_head:
                new_head = prev
            else:
                prev_tail.next = prev

            prev_tail = group_head

        prev_tail.next = curr
        return new_head
