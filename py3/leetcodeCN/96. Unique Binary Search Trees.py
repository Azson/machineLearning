#!/usr/bin/python
# -*- coding: utf-8 -*-


def numTrees(n):
    if n < 3:
        return n
    ans = 1
    for i in range(n-1):
        ans *= 3
    return (ans + 1) // 2


if __name__ == '__main__':
    while True:
        num = int(input())
        print(numTrees(num))
    pass