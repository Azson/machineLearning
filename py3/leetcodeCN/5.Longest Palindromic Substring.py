#!/usr/bin/python
# -*- coding: utf-8 -*-

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    dp = [[0 for i in range(length)] for j in range(length)]
    ans = s[0]
    for i in range(length):
        dp[i][i] = 1
        if i+1 < length and s[i] == s[i+1]:
            dp[i][i+1] = 1
            ans = s[i:i+2]
    for ln in range(3, length+1):
        for j in range(length-ln+1):

            if dp[j+1][j+ln-2] == 1 and s[j] == s[j+ln-1]:
                dp[j][j+ln-1] = 1
                if ln > len(ans):
                    ans = s[j:j+ln]
    return ans


def useLessSpace(s):
    length = len(s)
    ans = s[0]

    def posToLength(l, r):
        while l >= 0 and r < length and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1

    for i in range(length):
        l1 = posToLength(i, i)
        l2 = posToLength(i, i+1)
        ans = ans if len(ans) >= l1 else s[i-l1//2:i+l1//2+1]
        ans = ans if len(ans) >= l2 else s[i-l2//2+1:i+l2//2+1]

    return ans


#p[i]-1 is the length of the palindromic string in center of i
def monacher(s):
    length = len(s)
    str1 = ['@']
    for i in range(1, length+1):
        str1.extend('#')
        str1.extend(s[i-1])
    str1.extend('#')
    length2 = 2*length + 1
    p = [0 for i in range(length2)]
    mx = pos = 0
    ans = []
    #print(str1)
    for i in range(1, length2):
        p[i] = min(mx-i, p[2*pos - i]) if mx > i else 1
        while i-p[i] >= 0 and i+p[i] < length2 and str1[i-p[i]] == str1[i+p[i]]:
            p[i] += 1
        if p[i] + i > mx:
            mx = p[i]+i
            pos = i
        if len(ans) < p[i]*2:
            ans = str1[i-p[i]+1:i+p[i]]
    ans = list(filter(lambda x: x != '#' and x != '@', ans))
    #print(p)
    return ''.join(ans)




if __name__ == '__main__':
    while True:
        s = str(input())
        print(longestPalindrome(s))
        print(useLessSpace(s))
        print(monacher(s))
    pass