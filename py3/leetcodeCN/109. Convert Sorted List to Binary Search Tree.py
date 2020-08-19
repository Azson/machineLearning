# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        ls = []
        while head != None:
            ls.append(head.val)
            head = head.next

        ln = len(ls)

        def create_tree(l, r):
            if l > r:
                return None
            mid = (l+r) // 2
            now = ls[mid]
            node = TreeNode(now)

            node.left = create_tree(l, mid-1)
            node.right = create_tree(mid+1, r)
            return node

        return create_tree(0, ln-1)