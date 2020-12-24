# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月09日
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        hmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            if i < len(s) - 1 and hmap[s[i]] < hmap[s[i + 1]]:
                sum -= hmap[s[i]]
            else:
                sum += hmap[s[i]]
        return sum
