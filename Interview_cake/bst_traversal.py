class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def get_height(self, root):
        if root is None:
            return -1
        else:
            return 1 + max(self.get_height(root.left), self.get_height(root.right))
        
    def contains(self, root, n):
        if root is None: return False
        if root.data == n:
            return True
        elif n < root.data:
            return self.contains(root.left, n)
        else:
            return self.contains(root.right, n)
        
    def print_in_order(self, root):
        """
        The elements are processed in left-ROOT-right order.
        An inorder traversal of a BST will process the tree's elements in ascending order.
        """
        if root is not None:
            self.print_in_order(root.left)
            print(root.data),
            self.print_in_order(root.right)
            
    def print_pre_order(self, root):
        """
        The elements are processed ROOT-left-right order.
        Because a preorder traversal goes as deeply to the left as possible, it's also known as a
        depth-first-search or DFS.
        :param root:
        :return: None
        """
        if root is not None:
            print(root.data),
            self.print_pre_order(root.left)
            self.print_pre_order(root.right)
            
    def print_post_order(self, root):
        """
        The elements are processed in left-right-ROOT order.
        :param root:
        :return: None
        """
        if root is not None:
            self.print_post_order(root.left)
            self.print_post_order(root.right)
            print(root.data),

    @staticmethod
    def print_level_order(root):
        """
        BFS algorithm that processes the root, followed by the children of the root
        (from left to right), followed by the grandchildren of the root (from left to right), etc.
        Because a level-order traversal goes level-by-level, it's also known as a
        breadth-first-search (BFS).
        :param root:
        :return: None
        """
        if root is not None:
            queue = [root]
            while queue:
                node = queue.pop()
                print(node.data),
                if node.left is not None:
                    queue.insert(0, node.left)
                if node.right is not None:
                    queue.insert(0, node.right)


def main():
    """
    Objective
    Today, we're working with Binary Search Trees (BSTs).

    Input Format

    The locked stub code in your editor reads the following inputs and assembles them into a binary
    search tree:
    The first line contains an integer, , denoting the number of nodes in the tree.
    Each of the  subsequent lines contains an integer, , denoting the value of an element that must
    be added to the BST.

    Sample Input

    7
    3
    5
    2
    1
    4
    6
    7
    """
    numbers = int(input())
    my_tree = Solution()
    root = None
    for _ in range (numbers):
        data = int(input())
        root = my_tree.insert(root, data)
    height = my_tree.get_height(root)
    print('height = ', height)
    print('tree contains 5?', my_tree.contains(root, 5))
    print("\nIn Order:\n")
    my_tree.print_in_order(root)
    print("\nPre Order:\n")
    my_tree.print_pre_order(root)
    print("\nPost Order:\n")
    my_tree.print_post_order(root)
    print("\nLevel Order:\n")
    my_tree.print_level_order(root)


if __name__ == '__main__':
    main()
