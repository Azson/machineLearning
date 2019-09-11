# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def find_left(now, flag):
            if not now:
                return 0

            if not now.left and not now.right and flag:
                ret = now.val
            else:
                ret = 0

            ret += find_left(now.left, True)
            ret += find_left(now.right, False)

            return ret

        return find_left(root, False)