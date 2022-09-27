# 快慢指针法，快指针先走n步，然后快慢指针一起走，当快指针是链表尾部的最后一个元素时，慢指针指向元素的下一个元素就是需要删的那个元素。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

if __name__ == '__main__':
    list1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(5)))))
    solution = Solution()
    res = solution.removeNthFromEnd(list1,2)
    print(res)
