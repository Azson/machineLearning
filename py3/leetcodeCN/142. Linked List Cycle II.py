# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        pp = head
        circle = False
        while pp and pp.next and pp.next.next:
            p = p.next
            pp = pp.next.next
            if p == pp:
                circle = True
                break
        if not circle:
            return None

        p = head
        while p != pp:
            p = p.next
            pp = pp.next

        return p