print("Welcome to Python Lab!")

from binaryTree import BinaryTree
import random





tree = BinaryTree(root=5)
data = [random.randint(1, 100) for x in range(10)]
for i in data:
        tree.insertElement(i)

for i in range(len(data)):
        randIndex = random.randint(0, len(data) - 1)


# A List of Items
items = list(range(0, 57))
l = len(items)
tree.inorder_traversal()
tree.postorder_traversal()
tree.preorder_traversal()










