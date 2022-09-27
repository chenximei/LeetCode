class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root] #将二叉树放到一个列表里
        res = []
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if node:
                    layer.append(node.val) #存储当前层的值
                    next_queue += [node.left, node.right] #将下面所有的放到链表里
            queue = next_queue[:] #复制下面的树结构，更新队列
            if layer:
                res.append(layer[:]) #将此层的结点存起来，用append是将每层存储成为独立的列表
        return res

if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    solution = Solution1()
    res = solution.levelOrder(root)
    print(res)