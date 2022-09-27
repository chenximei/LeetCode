#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 23.09.22 9:25 PM
# @Author  : Chen Jinwei
# @FileName: 383 Ransom Note.py

import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = dict()
        for s in ransomNote:
            if s in hashmap:
                hashmap[s] += 1
            else:
                hashmap[s] = 1

        # check if the letter we need can be found in magazine
        for l in magazine:
            if l in hashmap:
                hashmap[l] -= 1

        for key in hashmap:
            if hashmap[key] > 0:
                return False

        return True

    def canConstruct1(self, ransomNote: str, magazine: str) -> bool:

        from collections import defaultdict

        hashmap = defaultdict(int)

        for x in magazine:
            hashmap[x] += 1

        for x in ransomNote:
            value = hashmap.get(x)
            if value is None or value == 0:
                return False
            else:
                hashmap[x] -= 1

        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        x = c1 - c2
        # x只保留值大于0的符号，当c1里面的符号个数小于c2时，不会被保留
        # 所以x只保留下了，magazine不能表达的
        if (len(x) == 0):
            return True
        else:
            return False

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:

        arr = [0] * 26

        for x in magazine:
            arr[ord(x) - ord('a')] += 1

        for x in ransomNote:
            if arr[ord(x) - ord('a')] == 0:
                return False
            else:
                arr[ord(x) - ord('a')] -= 1

        return True