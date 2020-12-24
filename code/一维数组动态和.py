# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月23日
"""


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums
