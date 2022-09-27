class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: Node) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0) #maxSum在这一步已经更新到了两边子树的最大值

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain) #最后返回的是根节点能提供的最大值，但是单独的子树可能更高，已在maxSum更新

        maxGain(root)
        return self.maxSum

if __name__ == '__main__':
    root = Node(-10, Node(9), Node(20, Node(15, Node(7))))
    solution = Solution()
    res = solution.maxPathSum(root)
    print(res)

