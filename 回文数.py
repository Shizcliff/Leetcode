# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月07日
"""

def isPalindrome(self,x):
    """
    :type x: int
    :rtype: bool
    """

    x = str(x)
    num = x[::-1]
    if num == x:
        return True
    else:
        return False