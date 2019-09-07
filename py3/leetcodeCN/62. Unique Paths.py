#!/usr/bin/python
# -*- coding: utf-8 -*-

def uniquePaths(m, n):
    dp = [[0 for i in range(n)] for j in range(m)]

    for i in range(0, m):
        for j in range(0, n):
            if i == 0:
                dp[0][j] = 1
            elif j == 0:
                dp[i][0] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp)
    return dp[m-1][n-1]

if __name__ == '__main__':
    while True:
        m = int(input())
        n = int(input())
        print(uniquePaths(m, n))
    pass