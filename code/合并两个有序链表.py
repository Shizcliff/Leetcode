# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月12日
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l3 = ListNode()
    node = l3

    while l1 and l2:
        if l1.val < l2.val:
            node.next,l1 = l1,l1.next
        else:
            node.next,l2 = l2,l2.next
        node = node.next
    if l1:
        node.next = l1
    if l2:
        node.next = l2

    return l3.next