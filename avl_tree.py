# AVL Tree implementation
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

def getHeight(root):
    if root == None:
        return 0
    return root.height

def rightRotate(y):

    # Create references
    x = y.left
    t2 = x.right

    # Actual Rotation
    y.left = t2
    x.right = y

    # Update heights
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1

    # Return the new root
    return x


def leftRotate(y):

    # Create references
    x = y.right
    t2 = x.left

    # Rotate
    y.right= t2
    x.left = y

    # Update heights
    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1

    # Return new root
    return x

def getBalance(root):
    if root == None:
        return 0
    return getHeight(root.left) - getHeight(root.right)


def insert(root, data):
    # Insert new element into the AVL tree
    if root == None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    else:
        return root

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    balance = getBalance(root)

    # Left left case
    if root.left != None:
        if balance > 1 and data < root.left.data:
            return rightRotate(root)

    # Left right case
        if balance > 1 and data > root.left.data:
            root.left = leftRotate(root.left)
            return rightRotate(root)

    # right right case
    if root.right != None:
        if balance < -1 and data > root.right.data:
            return leftRotate(root)

        if balance < -1 and data < root.right.data:
            root.right = rightRotate(root.right)
            return leftRotate(root)

    return root

def minValueNode(root):
    p = root;
    while p.left != None:
        p = p.left
    return p

def delete(data, root):
    if root == None:
        return
    if data < root.data:
        root.left = delete(data, root.left)
    elif data > root.data:
        root.right = delete(data, root.right)
    else:
        if root.left == None or root.right == None:
            temp = root.left if root.left != None else root.right

            if temp == None:
                temp = root
                root = None
            else:
                root = temp
        else:
            temp = minValueNode(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)

    if root == None:
        return root

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    balance = getBalance(root)

    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root


def pre_order(root):
    if root == None:
        return
    print(root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def testAVLTree():
    root = Node(9)
    data = [5,10,0,6,11,-1,1,2]
    for d in data:
        root = insert(root, d)
    print("Preorder traversal is")
    pre_order(root)
    print("\n")

    root = delete(10,root)
    print("Preorder traversal is")
    pre_order(root)
    print("\n")

testAVLTree()