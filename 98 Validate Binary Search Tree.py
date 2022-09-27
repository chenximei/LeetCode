class Solution:
    def isValidBST(self, root) -> bool:
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inorder = list()
        self.inorderTra(root, inorder)
        # print inorder
        for i in range(len(inorder) - 1):
            if inorder[i] >= inorder[i + 1]:
                return False
        return True

    def inorderTra(self, root, inorder):
        if not root:
            return None

        self.inorderTra(root.left, inorder)
        inorder.append(root.val)
        self.inorderTra(root.right, inorder)

        return
