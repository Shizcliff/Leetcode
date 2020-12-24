# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月24日
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        for i in range(len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i] == nums[j] and i < j:
                    num += 1
        return num