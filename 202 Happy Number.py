#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 23.09.22 4:59 PM
# @Author  : Chen Jinwei
# @FileName: 202 Happy Number.py

class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_happy(num):
            sum_ = 0

            # 从个位开始依次取，平方求和，这两部很重要，除余是取个位，整除10是取个位之外的前面的两位，到最后个位数，只有余数，整除10是0，就结束了
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        # 记录中间结果
        record = set()  # 用数组也行

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True

            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)

solution = Solution()
res = solution.isHappy(19)
print(res)