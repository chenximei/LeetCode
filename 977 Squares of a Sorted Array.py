#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 21.09.22 10:35 AM
# @Author  : Chen Jinwei
# @FileName: 977 Squares of a Sorted Array.py

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)  # 建立和nums一个维度的数组，不能直接写res = nums，是深拷贝，就算写也要写res = copy.copy(nums), 但是这个费时间

        l = 0
        r = len(nums) - 1

        i = len(nums) - 1

        while (l <= r): # 条件是l<=r, 因为两个指针最后会汇集到最小平方数那，如果不写等于就会错过最小平方数，导致新数组第一位数是错的
            if (nums[r] ** 2 > nums[l] ** 2):
                res[i] = nums[r] ** 2
                r -= 1
            else:
                res[i] = nums[l] ** 2
                l += 1
            i -= 1

        return res


solution = Solution()
solution.sortedSquares([-4,-1,0,3,10])
