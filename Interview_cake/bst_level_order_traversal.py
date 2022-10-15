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
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    @staticmethod
    def level_order(root):
        """
        A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes
        from left to right, top to bottom.
        :param root:
        :return:
        """
        queue = []
        if root is not None:
            queue.append(root)
            while queue:
                #===============================================================
                # /*Dequeue node and make it temp_node*/
                #===============================================================
                root = queue.pop()
                print(root.data, sep=' ', end=' ')
                #===============================================================
                # /*Enqueue left child */
                #===============================================================
                if root.left is not None:
                    queue.insert(0, root.left)
                #===============================================================
                # /*Enqueue right child */    
                #===============================================================
                if root.right is not None:
                    queue.insert(0, root.right)


if __name__ == '__main__':
    # Sample Input
    #
    # 6
    # 3
    # 5
    # 4
    # 7
    # 2
    # 1
    # Sample Output
    #
    # 3 2 5 1 4 7
    numbers = int(input())
    my_tree = Solution()
    node = None
    for _ in range(numbers):
        info = int(input())
        node = my_tree.insert(node, info)
    my_tree.level_order(node)
