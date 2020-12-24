# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月01日
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        m = ''
        length = 0
        for i in s:
            if i not in m:
                m += i
                length = max(length, len(m))
            else:
                m += i
                m = m[m.index(i) + 1:]
        return length
