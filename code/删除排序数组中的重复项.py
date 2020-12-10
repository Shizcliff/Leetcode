# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月14日
"""

def removeDuplicates(self,nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 0:
        return 0
    lenth = len(nums) - 1
    for i in range(lenth):
        if nums[lenth - i] == nums[lenth - i - 1]:
            del nums[lenth - i - 1]
    return len(nums)
