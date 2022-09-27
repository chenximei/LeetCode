#  初始树结点构建
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 右中左的遍历顺序
        if not root:
            return root
        self.s = 0

        def convert(node):
            if not node:
                return

            convert(node.right)
            node.val += self.s
            self.s = node.val
            convert(node.left)

        convert(root)
        return root

if __name__ == '__main__':
    root = Node(5, Node(3, Node(2), Node(1)), Node(6, right=Node(7, Node(8))))
    solution = Solution()
    res = solution.convertBST(root)
    print(res)