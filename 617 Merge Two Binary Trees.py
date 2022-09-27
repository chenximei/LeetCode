#  初始树结点构建
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

if __name__ == '__main__':
    root1 = Node(5, Node(3, Node(6), Node(8)), Node(2, right=Node(7, Node(4))))
    root2 = Node(-10, Node(-20), Node(3, Node(4, Node(5)))) #存疑
    solution = Solution()
    res = solution.mergeTrees(root1,root2)
    print(res)