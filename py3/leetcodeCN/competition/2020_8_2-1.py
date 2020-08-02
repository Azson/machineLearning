class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ln = len(arr)
        ret = 0
        for i in range(ln):
            for j in range(i+1, ln):
                for k in range(j+1, ln):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[i] - arr[k]) <= c and abs(arr[j] - arr[k]) <= b:
                        ret += 1
        
        return ret