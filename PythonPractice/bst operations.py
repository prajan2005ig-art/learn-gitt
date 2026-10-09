from collections import deque


class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Bst:
    def __init__(self):
        self.root = None

    def insert(self,root,value):
        if root is None:
            return node(value)

        if root.data > value:
            root.left = self.insert(root.left,value)

        else:
            root.right = self.insert(root.right,value)

        return root

    def search(self,root,value):
        if root is None:
            return " not found"

        if root.data == value:
            return "found"

        if root.data > value:
            return self.search(root.left,value)

        else:
            return self.search(root.right,value)




    def minimum(self,root):
        if root is None:
            return None

        while root.left is not None:
            root = root.left

        return root.data

    def maximum(self,root):
        if root is None:
            return None

        while root.right is not None:
            root = root.right

        return root.data

    def delete(self,root,value):
        if root is None:
            return None

        if root.data > value:
            root.left = self.delete(root.left,value)

        elif root.data < value:
            root.right = self.delete(root.right,value)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            else:
                successor = root.right

                while successor.left is not None:
                    succesor = succesor.left

                root.data = succesor.data
                root.right = self.delete(root.right,succesor.data)

        return root

    from collections import deque
    def levelOrder(self,root):
        if root is None:
            return

        queue = deque([root])

        while queue:
            current = queue.popleft()
            print(current.data)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)


bst = Bst()

values = [1,2,3,3,4,5,6,7,890,23,34]

for value in values:
    bst.root = bst.insert(bst.root,value)


levelorder = bst.levelOrder(bst.root)
print(bst.minimum(bst.root))
print(bst.maximum(bst.root))
print(bst.search(bst.root,4))
bst.root = bst.delete(bst.root,4)
bst.levelOrder(bst.root)
bst.root = bst.delete(bst.root,5)
bst.levelOrder(bst.root)
bst.root = bst.delete(bst.root,890 )
bst.levelOrder(bst.root)













