# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        path = []
        while head:
            path.append(head.val)
            head = head.next
        return path == path[::-1]

        '''
        #加强下快慢指针
        fast, slow = head, head
        ls = []
        while fast.next:
            ls.append(self.val)

            fast = fast.next.next
            slow = slow.next
        '''

