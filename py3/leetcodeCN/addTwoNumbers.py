#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, keke=None):
        self.val = x
        self.next = keke

    def print(self):
        now = self
        while now:
            print(now.val, end='')
            now = now.next
        print()


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        now = l3
        f = 0
        while l1 or l2:
            a1 = l1.val if l1 else 0
            a2 = l2.val if l2 else 0
            now.val = a1 + a2 + f
            f = now.val // 10
            now.val %= 10
            #print(f'now is {now.val} l1 is {l1.val}, l2 is {l2.val}')

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if not (l1 or l2):
                break
            now.next = ListNode(-1)
            now = now.next
        while f:
            now.next = ListNode(f%10)
            f = f // 10
            now = now.next

        return l3


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6))
    l1 = ListNode(5)
    l2 = ListNode(5)

    Solution().addTwoNumbers(l1, l2).print()