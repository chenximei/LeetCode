# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        result = ListNode(-1)
        cur = result
        p = list()
        for i in lists:
            if i:
                heapq.heappush(p, (i.val, i))
                print("i",type(i))
                print("i.val",type(i.val))

        while len(p) > 0:
            cur.next = heapq.heappop(p)[1]
            cur = cur.next
            # x = cur.next.val
            # print("x",type(x))
            # print("cur.next",type(cur.next))
            if cur.next:
                heapq.heappush(p, (cur.next.val, cur.next))  #heapq对压入堆的元组的第一个元素排序，只在python2中能用

        return result.next

if __name__ == '__main__':
    list1 = ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4))))
    list2 = ListNode(2, next=ListNode(7))
    list3 = ListNode(3, next=ListNode(5, next=ListNode(6)))
    lists = [list2,list1,list3]
    solution = Solution()
    res = solution.mergeKLists(lists)
    print(res)