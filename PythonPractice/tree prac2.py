from asyncio import queues


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

def preorder(root):
    if root is None:
        return

    print(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data)

#postorder(root)
#preorder(root)
#preorder(root)
from collections import deque# for levelorder traversal
def levelorder(root):
    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

levelorder(root)
