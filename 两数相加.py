# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年10月16日
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(self,l1: ListNode, l2: ListNode):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        return res