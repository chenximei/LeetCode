#  初始树结点构建
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

#方法一. 递归方式  （当然可以非递归解法，但是递归解法更为直观）

#  比较容易理解的是使用  双重递归解法，按sum差值  去 DFS 遍历判别即可。   但是要顾虑好从每个位置可以作为开始和结尾，所以要双重形式
#  时间复杂度为O(n^2)   空间复杂度最优为O(n^2)
class Solution(object):
    def pathSum(self, root, sum):
        if root == None:
            return 0
        x = self.count(root,sum)
        y = self.pathSum(root.left, sum)
        z = self.pathSum(root.right, sum)

        res = x + y + z
        #  这个是双重 递归的形式， 一方面是当前结点启动，另一方面是对于其孩子 也分别启动递归。
        return res

    def count(self, root, sum):
        if root == None:
            return 0
        a = int(root.val == sum)
        b = self.count(root.left, sum - root.val)
        c = self.count(root.right, sum - root.val)
        res = a + b + c
        # 直接的  余值判别，   如果余值对应  那就满足条件了,满足条件路径+1。    (当前满足条件后，还得继续走 ，因为还可以以当前为起点，进行往下查找路径。  所以是个多重的形式)
        return res

if __name__ == '__main__':
    root = Node(5, Node(3, Node(6), Node(8)), Node(2, right=Node(7, Node(4))))
    solution = Solution()
    res = solution.pathSum(root,8)
    print(res)