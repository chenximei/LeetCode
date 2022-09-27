#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 24.09.22 10:57 AM
# @Author  : Chen Jinwei
# @FileName: 541 Reverse String II.py

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """

        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)   # 要先转成字符串数组

        for cur in range(0, len(s), 2 * k): # 2k是步长
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])

        return ''.join(res) # 用空字符串将res中的字符串连接起来
    '''
    Python中join()方法的主要作用是以特定的字符或字符串作为分隔符（字符串）将若干字符串拼接在一起。
    其作用的对象可以是单独的一个字符串，也可以是一个字符串元组，字符串列表、字符串集合或字符串字典类型。
    '''

    def reverseStr1(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            x = s[:p]
            y = s[p:p2][::-1]   # [::-1]是把当前数组倒序输出
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s

solution = Solution()
res = solution.reverseStr1("abcdefg", 2)
print(res)