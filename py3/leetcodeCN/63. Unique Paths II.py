#!/usr/bin/python
# -*- coding: utf-8 -*-
def uniquePaths(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    dp = [[0 for i in range(n)] for j in range(m)]
    dp[0][0] = obstacleGrid[0][0] ^ 1
    for i in range(0, m):
        for j in range(0, n):
            if obstacleGrid[i][j] == 1 or (i == 0 and j == 0):
                continue
            elif i == 0:
                dp[0][j] = dp[0][j - 1]
            elif j == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    # print(dp)
    return dp[m - 1][n - 1]

if __name__ == '__main__':
    while True:
        m = int(input())
        n = int(input())
        print(uniquePaths(m, n))
    pass
