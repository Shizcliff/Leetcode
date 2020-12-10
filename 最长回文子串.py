# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月08日
"""

def longestPalindrome(self,s):
    """
    :type s: str
    :rtype: str
    """

    # 暴力破解法(超出时间限制)
    # if len(s) < 2:
    #     return s
    # max = s[0]
    # for i in range(len(s)):
    #     for j in range(i + 1, len(s)+1):
    #         zs = s[i:j]
    #         rs = zs[::-1]
    #         if zs == rs and len(rs) > len(max):
    #             max = rs
    # return max

    #动态规划法
    num = len(s)
    dp = [[False] * num for _ in range(num)]
    ans = ""
    for l in range(num):
        for i in range(num):
            j = i + l
            if j >= len(s):
                break
            if l == 0:
                dp[i][j] = True
            elif l == 1:
                dp[i][j] = (s[i] == s[j])
            else:
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j + 1]
    return ans