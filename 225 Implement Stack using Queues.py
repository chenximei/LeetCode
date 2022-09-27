#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 26.09.22 10:02 PM
# @Author  : Chen Jinwei
# @FileName: 225 Implement Stack using Queues.py
from collections import deque

class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):    # 把除最后一个元素的其他元素，都重新排队，就是先挪最左边的，放到最后，以此类推，
            # 直到最左边的是之前的最后的元素，但是此时队列后面的又是之前的顺序了，譬如说[1,2,3]变成[3,1,2]，[1,2]下一次pop依然要再排一次队
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.que[-1] # 因为stack的top是队列入口处的值，也就是数组最后一个值，所以直接输出[-1]位

    def empty(self) -> bool:
        return not self.que

stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()