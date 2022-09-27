#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 22.09.22 10:28 PM
# @Author  : Chen Jinwei
# @FileName: 24 Swap Nodes in Pairs.py

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next:
        #     return head

        dummy = ListNode(next=head)
        pre = dummy
        while pre.next and pre.next.next:   # 奇数/单元素链表的时候，最后pre.next.next是空，偶数/空链表的时候，最后pre.next是空，就可以结束了
            cur = pre.next
            post = pre.next.next    # pre, cur, post分别代表要交换的前面一位，和要交换的两个

            cur.next = post.next    # 三步，第一步，在2没变的时候，通过2，让1指向2的下一个3，
            # 第二步，让2指向1，
            post.next = cur
            # 第三步，让0指向2，也就是指向目前应该在1位的，最后把0挪两位，到下一对前面
            pre.next = post

            pre = pre.next.next

        return dummy.next
