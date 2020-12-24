# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月10日
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False
        hmap = {')': '(', '}': '{', ']': '['}
        stack = list()
        for i in s:
            if i in hmap:
                if not stack or stack[-1] != hmap[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
