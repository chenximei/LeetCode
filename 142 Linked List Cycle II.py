# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #边界条件 判别
        if not head or not head.next:
            return None
        #  (1)跟  141一样的，快慢指针法，如果快慢指针会和，那就是有环。
        slow, fast = head, head
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

            if slow == fast:
                break
        # 小过程吧，没环就可以退出了。
        if slow != fast:  # 链表无环
            return None

        #  (2)主要的地方，在确定有环后，   分别从fast与slow相遇点 、起点  开始走，两者每次走一步，当再次走到重合点，那就是 链表入环点，很经典的思路。
        fast = head
        while slow:
            if slow == fast:  # 此点即是环起点
                return slow
            slow = slow.next
            fast = fast.next


    def detectCycle1(self, head):

        low, fast = head, head
        while fast and fast.next:
            low = low.next
            fast = fast.next.next
            if low == fast:
                p = head
                q = fast
                while p != q:
                    p = p.next
                    q = q.next

                return q

        return None

if __name__ == '__main__':
    node = ListNode(1)
    list1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4,next=(node)))))
    node.next = list1
    list2 = ListNode(2, next=ListNode(7,next=(list1)))
    list3 = ListNode(3, next=ListNode(5, next=ListNode(6,next=(list2))))
    solution = Solution()
    res = solution.detectCycle(list3)
    print(res)