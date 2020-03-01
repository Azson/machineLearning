# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """

        dt = dict()
        def dfs(now_node, to_search):
            if now_node.val == to_search.val:
                to_search = to_search.next
                if to_search is None:
                    return True
            else:
                to_search = head

            if now_node in dt and to_search in dt[now_node]:
                return False
            f = False
            if now_node.left:
                f |= dfs(now_node.left, to_search)
                if not f and to_search != head:
                    f |= dfs(now_node.left, head)
            if not f and now_node.right:
                f |= dfs(now_node.right, to_search)
                if not f and to_search != head:
                    f |= dfs(now_node.right, head)

            if now_node not in dt:
                dt[now_node] = dict()
            dt[now_node][to_search] = f

            return f

        return dfs(root, head)