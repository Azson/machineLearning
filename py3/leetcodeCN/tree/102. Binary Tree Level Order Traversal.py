#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ls = [root] if root else []
        ans = []
        while len(ls) > 0:
            ln = len(ls)
            tmp = []
            for i in range(ln):
                now = ls.pop(0)
                tmp.append(now.val)
                if now.left:
                    ls.append(now.left)
                if now.right:
                    ls.append(now.right)
            ans.append(tmp)
        return ans


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
print(Solution().levelOrder(tree))

if __name__ == '__main__':
    pass