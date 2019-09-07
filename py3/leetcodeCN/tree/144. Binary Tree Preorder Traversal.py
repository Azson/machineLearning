#!/usr/bin/python
# -*- coding: utf-8 -*-

def preorderTraversal(root):
    ans = []
    ls = []
    while root or len(ls) > 0:
        if root:
            ans.append(root.val)
            ls.append(root.right)
            root = root.left
        else:
            root = ls.pop()
            root = root.right
    return  ans
if __name__ == '__main__':
    pass