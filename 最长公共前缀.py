# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月09日
"""

def longestCommonPrefix(self,strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1

    # if not strs: return ''
    # str = strs[0]
    # for i in range(1,len(strs)):
    #     index = 0
    #     while index < min(len(strs[i]),len(str)) and str[index] == strs[i][index]:
    #         index += 1
    #     str = str[:index]
    # return str