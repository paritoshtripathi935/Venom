'''
Problem Statement:

ther is bnary search tree. For a strictly binary search tree, a new procedure of removing all the leaf nodes of the tree is performed until the tree is
empty. 
the sequence of removal of the leaf nodes is maintained at each step. 
build the binary search tree from this removal sequence.

# Input Format:
an aaray Treeleafnodes of strings, where each string is a leaf node of the tree in the order of removal.
'''

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def postorder(root):
    # if root is None,return
    if root is None:
        return
    # traverse left subtree
    postorder(root.leftChild)

    # traverse right subtree
    postorder(root.rightChild)
    # print the current node
    print(root.data, end=" ,")


def insert(root, newValue):
    # if binary search tree is empty, create a new node and declare it as root
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    # if newValue is less than value of data in root, add it to left subtree and proceed recursively
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        # if newValue is greater than value of data in root, add it to right subtree and proceed recursively
        root.rightChild = insert(root.rightChild, newValue)
    return root


root = insert(None, 50)
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
print("Postorder traversal of the binary tree is:")
postorder(root)
