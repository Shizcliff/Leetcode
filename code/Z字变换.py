# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月08日
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # if len(s) == 0 or numRows <= 1:
        #     return s
        # sr = ''
        # hmap = {}
        # for i in range(numRows):
        #     hmap[i] = ''
        # for i in range(len(s)):
        #     if (i // (numRows - 1)) % 2 == 0:
        #         hmap[i % (numRows - 1)] += s[i]
        #     else:
        #         hmap[numRows - (i % (numRows - 1)) - 1] += s[i]
        # for i in range(numRows):
        #     sr += hmap[i]
        # return sr

        if len(s) == 0 or numRows <= 1:
            return s
        hmap = {}
        sr = ''
        for i in range(numRows):
            hmap[i] = ''
        i, flag = 0, -1
        for c in s:
            hmap[i] += c
            if i == 0 or i == (numRows - 1):
                flag = -flag
            i += flag
        for c in range(numRows):
            sr += hmap[c]
        return sr
