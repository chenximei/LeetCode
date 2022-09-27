#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 22.09.22 9:44 AM
# @Author  : Chen Jinwei
# @FileName: 203 Remove Linked List Elements.py
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(next=head) # 先设置假的头节点，指向head，保存证据
        cur = dummy # 再设置一个用来操作的，如果直接用head操作，那head.val = val的时候，没法删除自己
        while (cur.next != None):
            if (cur.next.val == val):
                cur.next = cur.next.next    # 这里后面不需要再加一句cur = cur.next，在cur已经把下一个替换成后面的之后，接着循环，
                # 判断cur.next不是val之后，会直接走else，由else去做这件事
            else:
                cur = cur.next
        return dummy.next

solution = Solution()
list1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
res = solution.removeElements(list1, 3)
print(res)


