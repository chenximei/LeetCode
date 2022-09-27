# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#  方法一，迭代的方式
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

#  方法二，栈的方式
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next

        newhead = stack[-1]
        p = newhead
        stack.pop()
        while stack:
            p.next = stack.pop()
            p = p.next

        p.next = None
        return newhead

#  方法三，迭代的方式
class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            tmp = cur.next #保存尾部
            cur.next = pre #逆转局部
            pre = cur #pre后移
            cur = tmp #cur后移
        return pre

    def reverseList1(self, head):   # 递归
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse(cur, pre):
            if not cur:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(temp, cur)

        return reverse(head, None)

if __name__ == '__main__':
    list1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    solution = Solution3()
    res = solution.reverseList(list1)
    print(res)