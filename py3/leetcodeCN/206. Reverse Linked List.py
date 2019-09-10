# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # die dai
        pre = None
        nxt = head.next
        while nxt:
            nxt = head.next
            head.next = pre

            pre = head
            head = nxt
        return pre

        '''
        #recursion
        def recur(node, pre):
            if not node.next:
                node.next = pre
                return node
            tmp = node.next

            node.next = pre
            return recur(tmp, node)

        return recur(head, None)
        '''
