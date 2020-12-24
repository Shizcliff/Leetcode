# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月24日
"""


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        result = 0
        for i in [start + 2 * i for i in range(n)]:
            result ^= i
        return result