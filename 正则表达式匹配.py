# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月07日
"""
import re
def isMatch(self,s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    #使用正则表达式
    # str = re.match(p,s)
    # if str is not None:
    #     if str.group() == s:
    #         return True
    #     else:
    #         return False
    # else:
    #     return False

    if not p:
        return not s  # 结束条件

    first_match = (len(s) > 0) and p[0] in {s[0], '.'}
    if len(p) >= 2 and p[1] == '*':
        return isMatch(s, p[2:]) or (first_match and isMatch(s[1:], p))
    return first_match and isMatch(s[1:], p[1:])