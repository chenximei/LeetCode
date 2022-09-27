class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        else:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

            if left and right:  # 一个在左子树，一个在右子树
                return root
            elif left:  # 都在左子树
                return left
            elif right:  # 都在右子树
                return right
            else:
                return

    def lowestCommonAncestor1(self, root: Node, p, q) -> Node:
        if not root or root.val == p or root.val == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return  # 1.
        if not left: return right  # 3.
        if not right: return left  # 4.
        return root  # 2. if left and right:


if __name__ == '__main__':
    root = Node(5, Node(3, Node(6), Node(8)), Node(2, right=Node(7, Node(4))))
    solution = Solution()
    res = solution.lowestCommonAncestor(root,6,8)
    print(res)