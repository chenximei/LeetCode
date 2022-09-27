#  初始树结点构建
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1

        dfs(root)
        return self.ans

if __name__ == '__main__':
    root = Node(5, Node(3, Node(6), Node(8)), Node(2, right=Node(7, Node(4))))
    solution = Solution()
    res = solution.diameterOfBinaryTree(root)
    print(res)
