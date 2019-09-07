# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = None
        pre = None
        while l1 and l2:

            if l1.val < l2.val:
                ch = l1.val
                l1 = l1.next

            else:
                ch = l2.val
                l2 = l2.next

            tmp = ListNode(ch)
            if not pre:
                pre = tmp
                if not ans:
                    ans = pre
            else:
                pre.next = tmp
                pre = tmp

        l1 = l1 if l1 else l2

        while l1:
            tmp = ListNode(l1.val)
            if not pre:
                pre = tmp
                if not ans:
                    ans = pre
            else:
                pre.next = tmp
                pre = tmp
            l1 = l1.next

        return ans