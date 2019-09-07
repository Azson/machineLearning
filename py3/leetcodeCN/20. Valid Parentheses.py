#!/usr/bin/python
# -*- coding: utf-8 -*-
def isValid(s):
    ls = []
    tmp = ['(', '[', '{', ')', ']', '}']
    for item in s:
        if item in tmp[:3]:
            ls.extend(item)
        elif len(ls) < 1 or tmp[tmp.index(item) - 3] != ls[-1]:
            return False
        else:
            ls.pop()
    return len(ls) == 0


if __name__ == '__main__':
    print(isValid(str(input())))
    pass