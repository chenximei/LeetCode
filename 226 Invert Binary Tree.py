class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution:
    def invertTree(self, root: Node) -> Node:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left, root.right = right, left
        return root

if __name__ == '__main__':
    root = Node(-10, Node(9), Node(20, Node(15, Node(7))))
    solution = Solution()
    res = solution.invertTree(root)
    print(res)

