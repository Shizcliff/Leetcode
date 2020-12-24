# -*- coding：utf-8 -*-
"""
作者：lby
日期：2020年12月22日
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        que = []
        res = []
        que.append(root)
        is_even = True

        while len(que) > 0:
            size = len(que)
            ls = [0] * size
            while size:
                size -= 1
                node = que[0];
                que.pop(0)
                ls[len(ls) - size - 1 if is_even else size] = node.val
                if node.left: que.append(node.left)
                if node.right: que.append(node.right)
            res.append(ls)
            is_even = not is_even

        return res
