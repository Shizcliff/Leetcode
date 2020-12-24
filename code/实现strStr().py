# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月25日
"""

import re


class Solution(object):
    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if not needle:
            return 0
        if not haystack:
            return -1
        answer = re.search(needle, haystack)
        if not answer:
            return -1
        else:
            return answer.span()[0]
