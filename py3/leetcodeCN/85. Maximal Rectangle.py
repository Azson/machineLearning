#!/usr/bin/python
# -*- coding: utf-8 -*-


def maximalRectangle(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0 for j in range(n)] for i in range(m)]
    dp[0][0] = 1 if matrix[0][0] == '1' else 0

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + 1 if matrix[i][0] == '1' else 0

    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + 1 if matrix[0][i] == '1' else 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1]) + 1



if __name__ == '__main__':
    pass