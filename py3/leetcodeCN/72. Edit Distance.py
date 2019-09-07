#!/usr/bin/python
# -*- coding: utf-8 -*-
def minDistance(word1, word2):
    len1 = len(word1)
    len2 = len(word2)

    dp = [[0 for j in range(len2+1)] for i in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1
    return dp[len1][len2]


if __name__ == '__main__':
    pass