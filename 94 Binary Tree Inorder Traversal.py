from Binary_Tree import Node

if __name__ == '__main__':
    right_tree = Node(6)
    right_tree.left = Node(2)
    right_tree.right = Node(4)

    left_tree = Node(5)
    left_tree.left = Node(1)
    left_tree.right = Node(3)

    tree = Node(11)
    tree.left = left_tree
    tree.right = right_tree

    left_tree = Node(7)
    left_tree.left = Node(3)
    left_tree.right = Node(4)

    right_tree = tree  # 增加新的变量
    tree = Node(18)
    tree.left = left_tree
    tree.right = right_tree
    tree.preorder()
    print()
