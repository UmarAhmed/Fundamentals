# BST requires:
#   all values to the left are smaller
#   all values to the right are larger
#   items are unique


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def get_height(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        elif root.val < val:
            root.right = self.insert(root.right, val)
        else:
            root.left = self.insert(root.left, val)

        return root


# Prints a tree PreOrder
def print_tree(root):
    if root is not None:
        print(root.val)
    if root.left is not None:
        print_tree(root.left)
    if root.right is not None:
        print_tree(root.right)


# prints a tree Inorder
def np(root):
    if root is None:
        return
    else:
        np(root.left)
        print(root.val)
        np(root.right)


# Returns true if k is in the tree which has root "root", and false otherwise
def search(root, k):
    if root is None:
        return False

    if root.val == k:
        return True
    else:
        return search(root.left, k) or search(root.right, k)


# returns sorted list from tree
def tree_to_list(root, lis=list()):
    if root is None:
        pass
    else:
        tree_to_list(root.left, lis)
        lis.append(root.val)
        tree_to_list(root.right, lis)

    return lis


# takes list of numbers, creates new tree, and returns the root node of the tree
def list_to_tree(l):
    tree = BST()
    current = tree.root
    for i in l:
        current = tree.insert(current, i)

    return current


# level order printing, starts from 0
def print_level(root, i):
    if root is None:
        pass
    if i == 1:
        print(root.data)
    else:
        print_level(root.left, i - 1)
        print_level(root.right, i - 1)