# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月14日
"""

def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    if len(nums) == 0:
        return 0
    lenth = len(nums) - 1
    for i in range(len(nums)):
        if nums[lenth - i] == val:
            del nums[lenth - i]
    return len(nums)