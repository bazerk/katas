def print_tree(node):
    if not node:
        return
    print node.value
    print 'going L'
    print_tree(node.left)
    print 'going R'
    print_tree(node.right)


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def recombine(inorder, preorder):
    if not preorder:
        return None
    root_value = preorder[0]
    inorder_split = inorder.split(root_value)

    left_stop = len(inorder_split[0]) + 1
    preorder_left = preorder[1:left_stop]
    preorder_right = preorder[left_stop:]

    node = Node(root_value)
    node.left = recombine(inorder_split[0], preorder_left)
    node.right = recombine(inorder_split[1], preorder_right)
    return node

##   A
## B   C
root = recombine('BAC', 'ABC')
print_tree(root)

##     A
##    B
##   C
root = recombine('CBA', 'ABC')
print_tree(root)

##     A
##       B
##         C
root = recombine('ABC', 'ABC')
print_tree(root)

root = recombine('rfeyd', 'erfdy')
print_tree(root)
