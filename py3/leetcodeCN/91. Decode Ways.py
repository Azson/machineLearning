#!/usr/bin/python
# -*- coding: utf-8 -*-


def numDecodings(s):
    length = len(s)
    dp = [0 for i in range(length)]
    if length == 1:
        return 0 if s[0] == '0' else 1
    dp[0] = 1
    dp[1] = 1 if int(s[:2]) > 26 or s[1] == '0' else 2
    f = True if int(s[:2]) == 0 or s[0] == '0' or (s[1] == '0' and int(s[:2]) > 26) else False

    for i in range(2, length):
        if s[i] != '0':
            dp[i] = dp[i - 1]
            if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]
        else:
            dp[i] = dp[i - 1] = dp[i - 2]
            f = True if s[i - 1] == '0' else f
            f = True if int(s[i - 1:i + 1]) > 26 else f

    # print(dp)
    return dp[length - 1] if not f else 0


if __name__ == '__main__':
    while True:
        s = str(input())
        print(f'ans is {numDecodings(s)}')
    pass