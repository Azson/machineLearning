#!/usr/bin/python
# -*- coding: utf-8 -*-


def maxDepth_digui(root):
    if root:
        return max(maxDepth_digui(root.left), maxDepth_digui(root.right)) + 1
    return 0


def maxDepth(root):
    ls = [root]
    ans = 0
    while len(ls) > 0:
        ans += 1
        la = len(ls)
        for i in range(la):
            root = ls[i]
            if root.left:
                ls.append(root.left)
            if root.right:
                ls.append(root.right)
        ls = ls[la:]
    return ans





if __name__ == '__main__':
    pass