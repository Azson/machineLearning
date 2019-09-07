#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ls = []
        ans = []
        pre = None
        while root or len(ls) > 0:
            if root:
                ls.append(root)
                root = root.left

            else:
                root = ls[-1]
                if root.right and root.right != pre:
                    root = root.right
                else:
                    ls.pop()
                    ans.append(root.val)
                    pre = root
                    root = None
        return ans

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def dfs(now, pos):
    if now and s1[pos-1] != 'null':
        now.x = int(s1[pos-1])
        if 2*pos <= len(s1) and s1[2*pos-1] != 'null':
            now.left = TreeNode(int(s1[2*pos-1]))
            dfs(now.left, 2*pos)
        if 2*pos+1 <= len(s1) and s1[2*pos] != 'null':
            now.right = TreeNode(int(s1[2*pos]))
            dfs(now.right, 2*pos+1)


s1 = input()[1:-1].split(',')

if len(s1[0]) == 0:
    tree = None
else:
    tree = TreeNode(int(s1[0]))
dfs(tree, 1)
print(Solution().postorderTraversal(tree))

if __name__ == '__main__':
    pass
#[3,9,20,null,null,15,7]

