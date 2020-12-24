# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月24日
"""


class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return command.replace('()', 'o').replace('(al)', 'al')
