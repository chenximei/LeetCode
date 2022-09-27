# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head): #哈希表
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    def hasCycle1(self, head): #快慢指针
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

if __name__ == '__main__':
    list = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    node = ListNode(1)
    list = ListNode(1, next=ListNode(2, next=ListNode(3, next=node)))
    node.next = list
    solution = Solution()
    res = solution.hasCycle(list)
    print(res)