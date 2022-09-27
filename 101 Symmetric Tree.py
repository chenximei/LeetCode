class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树

# class Solution(object):
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    def dfs(left,right):
        # 递归的终止条件是两个节点都为空
        # 或者两个节点中有一个为空
        # 或者两个节点的值不相等
        if not (left and right):
            return True
        if not (left or right):
            return False
        if left.value!=right.value:
            return False
        return dfs(left.left,right.right) and dfs(left.right,right.left)
    # 用递归函数，比较左节点，右节点
    return dfs(root.left,root.right)

if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('B', Node('C'), Node('A')))
    # solution = Solution()
    res = isSymmetric(root)
    print(res)