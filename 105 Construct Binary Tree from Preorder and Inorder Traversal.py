class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 首先是递归截止条件
        if not preorder:
            return None
        # 根据  先序遍历的位置找到 根节点。
        root = Node(preorder[0])
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1:]
        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1:]
        # 创建节点树   (不断嵌入搭建好整个树，注意  一个树下前序和中序的长度肯定是一致的)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    res = solution.buildTree(preorder,inorder)
    print(res)