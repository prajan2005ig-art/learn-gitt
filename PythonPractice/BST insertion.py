class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bst:
    def __init__(self):
        self.root = None

    def insert(self,root,value):#to enter the value in BST
       if root is None:
           return node(value)

       if root.data > value:
           root.left = self.insert(root.left,value)

       else:
           root.right = self.insert(root.right,value)
       return root

    def search(root,value):
        if root is None:
            return "not found"


        if root.data == value:
            return "found"

        if root.data > value:
            return self.search(root.left,value)

        else:
            return self.search(root.right,value)

    def minvalue(root):
        if root is None:
            return None

        while root.left is not None:
            root = root.left
        return root.data


    def maxvalue(root):
        if root is None:
            return
        while root.right is not None:
            root = root.right
        return root.data


    def delete(self,root,value):
        if root is None:#to delete
            return

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
                    successor = successor.left

                root.data = successor.data
                root.right = self.delete(root.right,successor.data)


    from collections import deque

    def levelorder(self,root=None):
        if root is None:
            return
        if not root:
            return
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()
            print(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

bst = Bst()

bst.root = bst.insert(bst.root,1)
bst.root = bst.insert(bst.root,2)
bst.root = bst.insert(bst.root,3)
bst.root = bst.insert(bst.root,4)

bst.levelorder()







