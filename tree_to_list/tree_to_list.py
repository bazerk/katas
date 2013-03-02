def print_tree(node):
    if not node:
        return
    print node.value
    print_tree(node.left)
    print_tree(node.right)


def print_list(node, forwards=True):
    while node is not None:
        print node.value
        node = node.right if forwards else node.left


def transform_to_list(node, prev=None):
    if not node:
        return prev
    left = node.left
    right = node.right
    node.left = prev
    if prev:
        prev.right = node
    prev = transform_to_list(left, node)
    return transform_to_list(right, prev)


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

root = Node(1,
    Node(2, Node(4), Node(5)),
    Node(3, Node(6), Node(7))
)

print "As tree"
print_tree(root)
print "transforming"
tail = transform_to_list(root)
print "As list"
print_list(root)
print "Backwards"
print_list(tail, False)
