class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr = sorted(arr)

        ans = []
        diff = 10**7
        for i in range(1, len(arr)):
            tmp = arr[i] - arr[i-1]
            if tmp <= diff:
                if tmp < diff:
                    diff = tmp
                    ans = []
                ans.append([arr[i-1], arr[i]])

        return ans
