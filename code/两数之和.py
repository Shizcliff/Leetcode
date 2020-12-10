# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年10月16日
"""

def twoSum(self,nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [hashmap.get(target - num),1]
            hashmap[num] = i

# class Solution:
#     def twoSum(nums,target):
#         lens = len(nums)
#         j=-1
#         for i in range(1,lens):
#             temp = nums[:i]
#             if (target - nums[i]) in temp:
#                 j = temp.index(target - nums[i])
#                 break
#         if j>=0:
#              return [j,i]
#
# print(Solution.twoSum([2,7,11,15],9))
