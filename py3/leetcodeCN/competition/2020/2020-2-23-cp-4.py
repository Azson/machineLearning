class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        def is_three_num(x):
            ret = 0
            for i in x:
                ret += int(i)
            return ret % 3 == 0

        def is_big(x, y):
            if len(x) != len(y):
                if len(x) > len(y):
                    return x
                return y

            return x if x > y else y

        n = len(digits)
        digits = sorted(digits, reverse=True)
        dp = [[""]*3 for i in range(n+1)]

        for i in range(1, n+1):
            dp[i][digits[i - 1] % 3] = str(digits[i - 1])
            for j in range(3):
                if j != digits[i - 1] % 3:
                    dp[i][j] = dp[i-1][j]
            for j in range(3):
                if  dp[i-1][(15-digits[i-1]+j)%3] != '':
                    dp[i][j] = is_big(dp[i][j], dp[i-1][(15-digits[i-1]+j)%3] + str(digits[i-1]))

            if i > 2:
                for j in range(3):
                    if  dp[i-2][(15-digits[i-1]+j)%3] != '':
                        dp[i][j] = is_big(dp[i][j], dp[i-2][(15-digits[i-1]+j)%3] + str(digits[i-1]))

        mx = dp[n][0]
        while n > 0 and not is_three_num(mx):
            mx = dp[n-1][0]
            n -= 1

        if n == -1:
            return ''
        if len(mx) > 0 and mx[0] == '0':
            return '0'

        return mx


if __name__ == '__main__':
    obj = Solution()
    digits = [7,1,2,4,0,0,4,0,3,8]
    print(obj.largestMultipleOfThree(digits))