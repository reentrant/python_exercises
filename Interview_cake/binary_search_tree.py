import collections
Node = collections.namedtuple('Node', ['left', 'right', 'value'])


def contains(root, value):
    "checks if a given binary search tree contains a given value."
    if root is None:
        return False
    else:
        if value == root.value:
            return True
        elif value < root.value:
            return contains(root.left, value)
        elif value > root.value:
            return contains(root.right, value)


if __name__ == '__main__':
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
    print(contains(n2, 3))
    print(contains(n2, 0))

    print(Node._fields)
