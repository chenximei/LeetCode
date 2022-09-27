class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

# 进行 中序遍历，  获取第k个遍历的值即可，不需要完全的遍历。   这里使用递归的方式实现中序遍历
# 时间复杂度为O(k),空间复杂度为O(N)
class Solution(object):
    def __init__(self):
        self.iter_num=0
        self.res=None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #  边界条件判别
        if not root:
            return
        #  左子树递归
        self.kthSmallest(root.left,k)

        #  中间位置的判别 和 计算。  中序遍历的判别计算部分
        self.iter_num+=1
        if self.iter_num==k:
            self.res=root.val

        # 比较核心的，进行k步即可，如果已经找到了，就不需要后面的递归查找了。
        else:
            #右子树递归
            self.kthSmallest(root.right,k)
        return self.res

if __name__ == '__main__':
    root = Node(-10, Node(-20), Node(3, Node(4, Node(5)))) #存疑
    solution = Solution()
    res = solution.kthSmallest(root,3)
    print(res)

