class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root
        # 先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right  # 把捋直的右子树备份一下

        root.right = root.left  # 把捋直的左子树放到右边
        root.left = None  # 记得把左子树置空
        while (root.right):  # 找到现在右子树的最后一个node
            root = root.right
        root.right = tmp  # 把捋直的原来的右子树接上去
        return root

    def flatten1(self, root: Node) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right


if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    solution = Solution()
    res = solution.flatten(root)
    print(res)