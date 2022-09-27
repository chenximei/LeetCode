#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 24.09.22 6:19 PM
# @Author  : Chen Jinwei
# @FileName: 151 Reverse Words in a String.py
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def removespace(s):
            slow = 0
            i = 0
            while i < len(s):   # 用while不用for，for会影响i的循环
                if s[i] != " ":
                    if slow != 0:
                        s[slow] = ' '
                        slow += 1
                    while i < len(s) and s[i] != ' ':
                        s[slow] = s[i]
                        i += 1
                        slow += 1
                i += 1
            return s[:slow]

        def reverse(s, left, right):
            while (left < right):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s

        s = list(s) # 先转换列表再操作
        s = removespace(s)
        s = reverse(s, 0, len(s)-1)
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s = reverse(s, start, i - 1)    # 注意输入是s，因为start和end都是对应到s里的index，如果只输入切片譬如s[start:i]，
                # left和right就不能是start和i-1
                start = i+1 # 注意start也要更新
            if i == len(s) - 1: # i在最后一位要单独讨论
                s = reverse(s, start, i)

        return ''.join(s)

    def reverseWords1(self, s: str) -> str:
        # method 1 - Rude but work & efficient method.
        s_list = [i for i in s.split(" ") if len(i) > 0]
        return " ".join(s_list[::-1])

solution = Solution()
res = solution.reverseWords("  we  are happy  ")
print(res)