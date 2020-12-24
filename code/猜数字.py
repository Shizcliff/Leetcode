# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月24日
"""


class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        num = 0
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                num += 1
        return num
