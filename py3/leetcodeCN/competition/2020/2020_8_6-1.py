#
# 
# @param n int整型 字符串长度n
# @param k int整型 循环右移次数k
# @return int整型
#
#

'''
1 2 3 4
3 4 1 2
2 1 4 3
1 2 3 4

1 2
2 1
1 2

1 2 3
2 3 1
3 2 1
1 2 3

1 2 3 4 5
3 4 5 1 2
2 1 5 4 3
1 2 3 4 5

1 2 3


1 2 3 4
3 4 1 2

'''


class Solution:
    def solve(self , n , k ):
        # write code here
        k %= n
        if k == 0:
            return 0
        if n <= 3:
            return n-1
        if k in [1, 2, n-1, n-2]:
            return 2
        return 3