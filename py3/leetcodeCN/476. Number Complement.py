#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# @ModuleName : 476. Number Complement
# @Function : 
# @Author : azson
# @Time : 2019/10/11 21:39
'''

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        op = 0
        tmp = num
        while num:
            op <<= 1
            op += 1
            num = num >> 1
        return op ^ tmp