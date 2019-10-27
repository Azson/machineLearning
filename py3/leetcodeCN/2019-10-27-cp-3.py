class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        cnt = len(arr)
        ans = 0
        pas = []

        for idx, item in enumerate(arr):
            if len(item) != len(set(item)):
                pas.append(idx)

        for i in range(1<<cnt):
            pos = 0
            new = []
            sz = 0
            while i:
                if i & 1:
                    if pos in pas or sz > 26:
                        break
                    new.append(arr[pos])
                    sz += len(arr[pos])
                i >>= 1
                pos += 1
            if i:
                continue
            new = ''.join(new)
            if len(new) == len(set(new)):
                ans = max(ans, len(new))
        return ans