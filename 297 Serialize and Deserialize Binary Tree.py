#  初始树结点构建
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution:

    #首先是 对 树的 先序操作式的序列化操作。
    def Serialize(self,root):

        # 我们的目标是对  root指向的树，  先序遍历的结果存到字符串中
        serializeStr=''

        #边界条件
        if root==None:
            return '#'

        #这里使用 非递归的先序遍历方式     利用栈的形式
        stack=[]
        while root or stack:
            while root:
                # 先序就是 先进行 输出操作
                serializeStr+=str(root.val)+','

                #非递归的方式， 打印后，使劲往左一直走
                stack.append(root)
                root=root.left

            # 当往左走到极端时，开始往右边进行行走，这里有个pop要注意下。这里  #,是考虑遇到空的情况。
            serializeStr+='#,'
            root=stack.pop()#非常特别的pop位置，这里是获取之前上一次的 中间位置，这个很重要，往右走也得是从底往上逐步的
            root=root.right

        #现在 的 serializeStr 保存的就是合适的遍历结果。
        serializeStr=serializeStr[:-1]

        return serializeStr


    # 对于给定的序列  字符串s  进行  反序列成 二叉树。    主函数部分
    def Deserialize(self,s):
        serialize=s.split(',')
        #针对  切分好后的字符序列 进行 转成二叉树。    这里0是序列索引中的定位，首先肯定是从根部开始的。

        tree,sp=self.deserial(serialize,0)
        return tree

    #主要进行转换的部分     这里主要使用递归性质的转换方法       其中s是整个序列，sp是序列中对应的索引定位
    def deserial(self,s,sp):
        #边界 条件， 如果  索引位置异常   或者   索引定位为#,说明到边界位置了，那么当前不进行构建。
        if sp>=len(s) or s[sp]=='#':
            return None,sp+1

        node=Node(int(s[sp]))

        #这就是标准的 构建树的过程，  注意这里sp是在递归中的全局变量，所以同样的 不断增加的先左后右的 进行查看  和树的融入。
        sp+=1
        #注意这里是  序列化的反过程， 之前是不断的先看和放左边的，所以合理也是使用递归的方式先还原左边的。    递归其实和使用栈是同样的实现先序遍历的方法。
        node.left,sp=self.deserial(s,sp)
        node.right,sp=self.deserial(s,sp)

        #这里的 node  其实就是现有的构建树的结果。
        return node,sp

if __name__ == '__main__':
    root = Node(5, Node(3, Node(6), Node(8)), Node(2, right=Node(7, Node(4))))
    solution = Solution()
    res = solution.Serialize(root)
    res = solution.Deserialize(res)
    print(res)