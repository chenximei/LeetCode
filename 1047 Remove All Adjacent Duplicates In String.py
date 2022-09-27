#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 27.09.22 9:54 AM
# @Author  : Chen Jinwei
# @FileName: 1047 Remove All Adjacent Duplicates In String.py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item: # 注意条件选择，在栈不为空的前提下，如果栈顶元素和s[i]相等，则栈弹出，此处不能用栈不为空和不相等组合，
                # 因为栈为空和不相等这两个条件是单独成立的，而且他们俩的结果都是append新s[i]
                res.pop()
            else:
                res.append(item)
        return "".join(res)  # 字符串拼接

    # 方法2，双指针模拟栈
    def removeDuplicates1(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(res)

        while fast < length:
            # 如果一样直接换，不一样会把后面的填在slow的位置
            res[slow] = res[fast]

            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1

        return ''.join(res[0: slow])