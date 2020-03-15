# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def dfs(now):

            if now.left is None and now.right is None:
                sort_ls.append(now)
                return
            if now.left:
                dfs(now.left)
            sort_ls.append(now)
            if now.right:
                dfs(now.right)

        def make_new_tree(l, r):
            if l >= r:
                return None

            m = (r + l) // 2
            now = sort_ls[m]
            now.left = make_new_tree(l, m)
            now.right = make_new_tree(m + 1, r)
            return now

        sort_ls = []
        dfs(root)
        ln = len(sort_ls)
        root = make_new_tree(0, ln)

        return root
