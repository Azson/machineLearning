#!/usr/bin/python
# -*- coding: utf-8 -*-


def maxProfit(prices):
    m = len(prices)
    ans = mx = 0
    mn = 999999
    for i in range(m):
        if mn > prices[i]:
            mn = prices[i]
            mx = prices[i]
        if mx < prices[i]:
            mx = prices[i]
            if mx - mn > ans:
                ans = mx-mn
    return ans


if __name__ == '__main__':
    while True:
        ls = str(input())[1:-1].split(',')
        ls = list(map(lambda x:int(x), ls))
        print(ls)
        print(maxProfit(ls))
    pass