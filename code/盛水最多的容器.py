# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年11月14日
"""


class Solution(object):
    def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) <= 1:
            return -1
        maxV, left, right = 0, 0, len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            maxV = max(maxV, h * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxV

        # 暴力破解法，超出时间限制，不可取
        # if len(height) <= 1:
        #     return -1
        # max, left, right = 0, 0, 0
        # for i in range(len(height) - 1):
        #     for j in range(i, len(height)):
        #         if height[i] <= height[j] and (height[i] * (j - i)) > max:
        #             max = height[i] * (j - i)
        #             left, right = i, j
        #         if height[i] >= height[j] and (height[j] * (j - i)) > max:
        #             max = height[j] * (j - i)
        #             left, right = i, j
        # return max
