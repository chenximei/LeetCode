#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 22.09.22 12:03 AM
# @Author  : Chen Jinwei
# @FileName: 59 Spiral Matrix II.py
class Solution:
    def generateMatrix(self, n: int):
        nums = [[0] * n for _ in range(n)]  # 每行是[0] * n，for后面_意思是，这句重复n次，不用单独设变量
        startx, starty = 0, 0               # 每一个循环每一个圈的起始位置
        loop, mid = n // 2, n // 2          # loop是要转几圈，迭代次数、mid是n为奇数时，矩阵的中心点，奇数时转圈不包括中心点，得在最后单独给中心点赋值
        count = 1                           # 计数

        for offset in range(1, loop + 1) :      # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset) :    # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset) :    # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1) : # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1) : # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1         # 更新起始点
            starty += 1

        if n % 2 != 0 :			# n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums