#!/usr/bin/python
# -*- coding: utf-8 -*-


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def generateTrees(n):
    vis = [0 for i in range(n+1)]

    def dfs(pos):
        for i in range(n):
            if vis[i] == 0:
                vis[i] = 1
                dfs()


if __name__ == '__main__':
    pass