#!/usr/bin/python
# -*- coding: utf-8 -*-

def minDepth(root):
    ls = [root]
    ans = 0
    while len(ls) > 0:
        ans += 1
        la = len(ls)
        for i in range(la):
            root = ls[i]
            if not (root.left and root.right):
                return ans+1
            if root.left:
                ls.append(root.left)
            if root.right:
                ls.append(root.right)

        ls = ls[la:]
    return ans

if __name__ == '__main__':
    pass