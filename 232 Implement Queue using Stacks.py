#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 26.09.22 9:28 PM
# @Author  : Chen Jinwei
# @FileName: 232 Implement Queue using Stacks.py
class MyQueue:

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())  # 把stackin清空，要pop，同时反序填满stackout
            return self.stack_out.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.pop()    # 注意这里是self.pop()不是self.stack_out.pop()，因为pop()函数里有对于empty情况的判断
        self.stack_out.append(ans)  # 还要把它放回去，因为只是想知道值，而不是弹出
        return ans

    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)

queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
queue.pop()
queue.pop()
queue.empty()
queue.push(1)
queue.peek()