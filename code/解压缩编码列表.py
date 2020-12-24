# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月24日
"""

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sum(([b] * a for a, b in zip(nums[::2], nums[1::2])), [])