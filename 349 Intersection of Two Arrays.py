#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 23.09.22 2:22 PM
# @Author  : Chen Jinwei
# @FileName: 349 Intersection of Two Arrays.py

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))    # 两个数组先变成集合，求交集后还原为数组