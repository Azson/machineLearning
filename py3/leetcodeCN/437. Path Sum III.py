# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        def recur_cnt(now, res):
            if not now:
                return 0
            ret = 1 if res == now.val else 0

            ret += recur_cnt(now.left, res - now.val)
            ret += recur_cnt(now.right, res - now.val)

            return ret

        return recur_cnt(root, sum) + \
               self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

