# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dic = {}
        p = headA
        while p:
            dic[p] = 1
            p = p.next
        p = headB
        while p:
            if p in dic:
                return p
            p = p.next
        return None

    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        """
               根据快慢法则，走的快的一定会追上走得慢的。
               在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。

               那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
               位置相遇
        """
        curA = headA
        curB = headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA


if __name__ == '__main__':
    list1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    list2 = ListNode(2, next=ListNode(7,next=(list1)))
    list3 = ListNode(3, next=ListNode(2, next=ListNode(3,next=(list1))))
    solution = Solution()
    res = solution.getIntersectionNode1(list1,list3)
    print(res)
