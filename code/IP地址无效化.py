# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月24日
"""


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = ''
        for i in range(len(address)):
            if address[i] == '.':
                result += '[.]'
            else:
                result += address[i]
        return result
