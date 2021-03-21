#
# 计算最小交换次数
# @param firstRow int整型一维数组 第一行的身高数据
# @param secondRow int整型一维数组 第二行的身高数据
# @return int整型
#
class Solution:
    def arrange(self , firstRow , secondRow ):
        # write code here
        n = len(firstRow)
        dp = [[n+1, n+1] for i in range(n)]
        dp[0][0], dp[0][1] = 0, 1

        for i in range(1, n):
            if firstRow[i] < firstRow[i-1] and secondRow[i] > secondRow[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][0])
            if firstRow[i] < secondRow[i-1] and secondRow[i] > firstRow[i-1]:
                dp[i][0] = min(dp[i][0], dp[i-1][1])
            if secondRow[i] < firstRow[i-1] and firstRow[i] > secondRow[i-1]:
                dp[i][1] = min(dp[i][1], dp[i-1][0] + 1)
            if secondRow[i] < secondRow[i-1] and firstRow[i] > firstRow[i-1]:
                dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)
        ans = min(dp[n-1])
        if ans == n+1:
            return -1
        return ans