#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 27.09.22 10:37 AM
# @Author  : Chen Jinwei
# @FileName: 150 Evaluate Reverse Polish Notation.py
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(i)
            else:
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(eval(f'{num2} {i} {num1}')))   # f"{}"是把变量放里边，带入变量本来的值，eval()是计算字符串表达式
        return int(stack.pop())

solution = Solution()
solution.evalRPN(["2","1","+","3","*"])