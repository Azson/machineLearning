#!/usr/bin/python
# -*- coding: utf-8 -*-
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ls = []
        for item in tokens:
            #print(f'item {item} ls {ls}')
            if item[-1] >= '0' and item[-1] <= '9':
                ls.append(int(item))
            else:
                if item == '+':
                    ls[-2] = ls[-2] + ls[-1]
                elif item == '-':
                    ls[-2] = ls[-2] - ls[-1]
                elif item == '*':
                    ls[-2] = ls[-2] * ls[-1]
                elif item == '/':
                    tmp = -1 if ls[-2] * ls[-1] < 0 else 1

                    ls[-2] = abs(ls[-2]) // abs(ls[-1]) * tmp

                ls.pop()
        return ls[0]

print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
if __name__ == '__main__':
    pass