class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

    def maxDepth1(self, root):
        stack = []  # 定义一个空栈，栈中的元素是结点及其对应的深度
        if root:  # 如果根结点不为空
            stack.append((root, 1))  # 则将根节点及其对应深度1组成的元组入栈
        max_depth = 0  # 初始化最大深度为零
        while stack:  # 当栈非空时
            tree_node, cur_depth = stack.pop()  # 弹出栈顶结点及其对应的深度
            if tree_node:  # 如果该结点不为空
                max_depth = max(max_depth, cur_depth)  # 更新当前最大深度，如果该结点深度更大的话
                stack.append((tree_node.left, cur_depth + 1))  # 将该结点的左孩子结点及其对应深度压入栈中
                stack.append((tree_node.right, cur_depth + 1))  # 将该结点的右孩子结点及其对应深度压入栈中
        return max_depth

if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    solution = Solution()
    res = solution.maxDepth1(root)
    print(res)