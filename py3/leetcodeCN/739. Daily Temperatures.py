class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []

        for idx, val in enumerate(T):
            while stack and val > stack[-1][0]:
                tmp = stack[-1]
                stack.pop(-1)
                ans[tmp[1]] = idx-tmp[1]
            stack.append((val, idx))
        return ans

if __name__ == '__main__':
    ls =  [73,74,75,71,69,72,76,73]
    # ls = [33, 33, 33, 33, 33]
    obj = Solution()
    print(obj.dailyTemperatures(ls))