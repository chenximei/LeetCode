#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 22.09.22 9:17 PM
# @Author  : Chen Jinwei
# @FileName: 707 Design Linked List.py

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        # 之后在用到所有这两个属性值和内部函数，都要写self再调用
        self.dummy = ListNode(0)    # 建立虚拟头节点，即头结点前面的指向头节点的
        self.size = 0   # 链表长度，初始为0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index>=self.size:
            return -1
        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        return cur.next.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        # cur = dummy
        # newNode = ListNode(val)
        # newNode.next = cur.next
        # cur.next = newNode
        self.addAtIndex(0,val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        # cur = dummy
        # newNode = ListNode(val)
        # while cur.next != Null:
        #     cur = cur.next
        # cur.next = newNode
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>self.size: # 注意这里是 > 不是 >=，因为插入位置可以是超出最后index的，也就是如果在tail插入的话，index = size
            return -1
        cur = self.dummy
        newNode = ListNode(val)
        while index:
            cur = cur.next
            index -= 1
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index>=self.size:
            return -1
        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1

new = MyLinkedList()
new.addAtHead(1)
new.addAtTail(2)
new.addAtIndex(2,3)
print(new)