#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 21.09.22 10:25 PM
# @Author  : Chen Jinwei
# @FileName: 209 Minimum Size Subarray Sum.py
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        # 定义一个无限大的数
        res = float("inf")
        Sum = 0
        index = 0
        for i in range(len(nums)):
            Sum += nums[i]
            while Sum >= s:
                res = min(res, i-index+1)   # 当前框内长度为 i - index + 1
                Sum -= nums[index]
                index += 1
        return 0 if res==float("inf") else res  # 最后要判断，是否数组里所有数加起来够target，有可能不够，不够的话一直没进入while循环，
        # 所以subset的长度一直是初始值inf