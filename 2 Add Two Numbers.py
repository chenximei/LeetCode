# 类似于纸上计算两个数字的和，首先从最低有效位也就是列表L1 和 L2 的表头开始相加。
# 由于每位数字都应当处于 0…9 的范围内，因此两个数字的和时可能会出现“溢出”。例如，5 + 7 = 12。
# 在这种情况下，将当前位的数值设置为 22，并将进位 carry=1 带入下一次迭代。进位 carry 必定是 0 或 1，
# 这是因为两个数字相加（考虑到进位）可能出现的最大和为 9 + 9 + 1 = 19。
# 思路：
#    先判断一下哪个链表长，然后用交换的方法确保一定是l1更长。
#    然后把l2的值加到l1上，全部加完之后遍历l1处理进位，记得处理最后一位需要进1的特殊情况。【控制进位并相加到 到L1链表上】
#   链表两数相加：carry存储进位，res存储当前位值，
#       res = (l1->val+l2->val+carry)%10，carry = (l1->val+l2->val+carry)/10；
#       ListNode* tmpnode=new ListNode(res);
#       PS：在两链表遍历完之后需要判断一下carry（即是否有最高位进位）


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        length1, length2 = 0, 0
        p = l1
        while p:
            length1 += 1
            p = p.next
        p = l2
        while p:
            length2 += 1
            p = p.next
        if length1 < length2:
            l1, l2 = l2, l1 #将l1设置成更长的链表

        p1, p2 = l1, l2
        c = 0
        while p2:
            p1.val += p2.val
            p1 = p1.next
            p2 = p2.next  #先加完更短的l2
        p1 = l1
        while p1:
            p1.val += c  #先加上一轮的进位再统一处理
            c = 0 #设置当前进位为0
            if p1.val > 9:
                p1.val -= 10
                c = 1  #处理当前数和进位
            if not p1.next and c: #处理最高位进位情况，如果链表没有下一个元素而进位有1则添加一位进位
                p1.next = ListNode(1)
                break
            p1 = p1.next
        return l1

    def addTwoNumbers1(self,list1,list2):
        head1 = list1
        head2 = list2

        firstNum = ""
        secondNum = ""
        while head1:
            firstNum += str(head1.val)
            head1 = head1.next

        firstNum = int(firstNum[::-1])
        print(firstNum)

        while head2:
            secondNum += str(head2.val)
            head2 = head2.next

        secondNum = int(secondNum[::-1])

        finalNum = str(firstNum + secondNum)

        root = None
        for i in range(len(finalNum)):
            temp = ListNode(0)
            temp.val = finalNum[i]
            temp.next = root
            root = temp
        return root

    def addTwoNumbers2(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10) #除余，divmod(7, 2) -> (3, 1)
            n.next = ListNode(val)
            # n.val = val
            n = n.next
        return root.next

if __name__ == '__main__':
    list1 = ListNode(5, next=ListNode(3, next=ListNode(6, next=ListNode(8))))
    list2 = ListNode(2, next=ListNode(3, next=ListNode(4, next=ListNode(7))))
    solution = Solution()
    res = solution.addTwoNumbers2(list1,list2)
    while res:
        print(res.val)
        res = res.next