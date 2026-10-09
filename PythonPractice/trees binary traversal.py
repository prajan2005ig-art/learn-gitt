class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

def preorder(root):
    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)

#preorder(root)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)

#postorder(root)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

#inorder(root)

from collections import deque

def level_order(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

level_order(root)
