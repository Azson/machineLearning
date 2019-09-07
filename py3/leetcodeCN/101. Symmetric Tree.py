# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def cmp(self, x, y):
        if x and y:
            return x.val == y.val and \
               self.cmp(x.left, y.right) and self.cmp(x.right, y.left)
        return x == y


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        return self.cmp(root.left, root.right)
