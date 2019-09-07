#!/usr/bin/python
# -*- coding: utf-8 -*-


def minimumTotal(triangle):
    m = len(triangle)
    for i in range(m-2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j] , triangle[i+1][j+1] )
    return triangle[0][0]


if __name__ == '__main__':
    pass