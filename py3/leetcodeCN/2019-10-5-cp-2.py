# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """

        ans = False

        def dfs_find(now, val):
            if not now:
                return False
            if now.val == val:
                return True
            if now.val < val:
                return dfs_find(now.right, val)
            elif now.val > val:
                return dfs_find(now.left, val)

        def dfs_rec(now):
            if not now:
                return False
            ret = dfs_find(root2, target - now.val)
            if not ret:
                ret = dfs_rec(now.left)
                if not ret:
                    ret = dfs_rec(now.right)
            return ret

        return dfs_rec(root1)