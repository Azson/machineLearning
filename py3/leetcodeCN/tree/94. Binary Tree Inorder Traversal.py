#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

ans = []
def inorderTraversal_digui(root):
    if root:
        inorderTraversal_digui(root.left)
        ans.append(root.val)
        inorderTraversal_digui(root.right)
    return ans

def inorderTraversal(root):
    ans = []
    ls = []
    while root or len(ls) > 0:
        if root:
            ls.append(root)
            root = root.left
        else:
            root = ls.pop()
            ans.append(root.val)
            root = root.right
    return ans
if __name__ == '__main__':
    pass