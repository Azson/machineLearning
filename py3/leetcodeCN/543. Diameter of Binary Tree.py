# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.lg = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        #程序应该去符合思考，而不是符合当前“输出”
        def dfs(now):
            if not now:
                # print(now.val, depth)
                return 0

            l = dfs(now.left)
            r = dfs(now.right)

            self.lg = max(self.lg, l + r)

            return max(l, r) + 1

        dfs(root)

        return self.lg