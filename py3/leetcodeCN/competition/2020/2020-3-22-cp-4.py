class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        ln = len(s)
        nxt = [0 for i in range(ln+5)]
        j = 0
        for i in range(2, ln+1):
            while j and s[j] != s[i-1]:
                j = nxt[j]
            if s[j] == s[i-1]:
                j+=1
            nxt[i] = j
        ans = []
        for i in range(nxt[ln]):
            ans.append(s[i])

        return ''.join(ans)
