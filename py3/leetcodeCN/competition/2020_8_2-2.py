class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        ln = len(arr)
        ans = arr[0]
        max_c = 0
        
        for i in range(1, ln):
            if arr[i] > ans:
                ans = arr[i]
                max_c = 1
            else:
                max_c += 1
            if max_c == k:
                break
        
        return ans