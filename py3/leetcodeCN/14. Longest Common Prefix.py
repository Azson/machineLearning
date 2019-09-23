class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        ans = len(strs[0])

        for i in range(1, len(strs)):
            ln = min(min(strs[0], strs[1]), ans)

            for j in range(ln):
                if strs[0][j] != strs[i][j]:
                    ans = j
                    break
            if not ans:
                return ""
        return strs[0][:ans]