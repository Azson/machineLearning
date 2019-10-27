"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """

        ans = []
        flag = False

        for x in range(1, 1001):
            if flag:
                break
            for y in range(1, 1001):
                tmp = customfunction.f(x, y)
                #print(x, y, tmp)

                if tmp >= z:
                    if tmp == z:
                        ans.append([x, y])
                    if y == 1:
                        flag = True
                    break

        return ans