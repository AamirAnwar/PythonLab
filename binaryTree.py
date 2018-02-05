'''Implementation of a binary tree in python'''

from __future__ import print_function
from time import sleep
class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "[{}]".format(self.data)

class BinaryTree:
    def __init__(self, root=None):
        self.root = None

    def isEmpty(self):
        return True if not self.root else False

    def insertElement(self,data):
       self.root = self.insertUtil(self.root,data)

    def insertUtil(self, root, data):
        if not root:
            print("Added {} to the tree!".format(data))
            return TreeNode(data)
        if data < root.data:
            root.left = self.insertUtil(root.left, data)
        else:
            root.right = self.insertUtil(root.right, data)
        return root

    def inorder_util(self, root):
        if not root:
            return
        self.inorder_util(root.left)
        print(" {} ".format(root.data),end=' -> ')
        self.inorder_util(root.right)


    def postorder_util(self, root):
        if not root:
            return
        print(" {} ".format(root.data),end=' -> ')
        self.postorder_util(root.left)
        self.postorder_util(root.right)

    def preorder_util(self, root):
        if not root:
            return
        self.preorder_util(root.left)
        self.preorder_util(root.right)
        print(" {} ".format(root.data),end=' -> ')




    def inorder_traversal(self):
        print("\nPerforming Inorder Traversal...")
        sleep(1)
        self.inorder_util(self.root)

    def postorder_traversal(self):
        print("\nPerforming Postorder Traversal...")
        sleep(1)
        self.postorder_util(self.root)

    def preorder_traversal(self):
        print("\nPerforming Preorder Traversal...")
        sleep(1)
        self.preorder_util(self.root)