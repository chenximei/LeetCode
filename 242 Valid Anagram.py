#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 23.09.22 2:09 PM
# @Author  : Chen Jinwei
# @FileName: 242 Valid Anagram.py
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(s[i]) - ord("a")] += 1
        print(record)
        for i in range(len(t)):
            record[ord(t[i]) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True

    def isAnagram1(self, s: str, t: str) -> bool:
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for x in s:
            s_dict[x] += 1

        for x in t:
            t_dict[x] += 1

        return s_dict == t_dict