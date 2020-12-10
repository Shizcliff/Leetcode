# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月06日
"""

def reverse(self,x):
    """
    :type x: int
    :rtype: int
    """

    num = str(x) if x > 0 else str(-x) + '-'
    num = int(num[::-1])
    return num if num > -2 ** 31-1 and num < 2 ** 31 else 0

