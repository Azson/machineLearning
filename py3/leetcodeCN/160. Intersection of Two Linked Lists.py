# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        pa, pb = headA, headB
        f = False
        while pa != pb:
            pa, pb = pa.next, pb.next
            if not pa:
                pa = headB
                if f:
                    return None
                f = True
            if not pb:
                pb = headA
        return pa


