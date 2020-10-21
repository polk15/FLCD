class Node:
    def __init__(self, index=-1, symbol=""):
        self.left = None
        self.right = None
        self.index = index
        self.symbol = symbol


class BST:
    def __init__(self):
        self.count = 0
        self.root = None

    def insert_recursive(self, root, node):
        if root is None:
            self.root = node
        else:
            if root.symbol < node.symbol:
                if root.right is None:
                    root.right = node
                else:
                    self.insert_recursive(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert_recursive(root.left, node)

    def in_order_print(self, root):
        if root:
            self.in_order_print(root.left)
            print(f"Symbol: {root.symbol} Code: {root.index}")
            self.in_order_print(root.right)

    def search_recursive(self, root, symbol):
        if root is None or root.symbol == symbol:
            return root

        if root.symbol < symbol:
            self.search_recursive(root.right, symbol)
        else:
            self.search_recursive(root.left, symbol)

        return -1

    def search(self, symbol):
        return self.search_recursive(self.root, symbol)

    def insert(self, key):
        index = self.search(key)

        if index != -1 and index is not None:
            return index.index
        else:
            self.insert_recursive(self.root, Node(self.count, key))
            self.count += 1
            return self.count - 1

    def print(self):
        self.in_order_print(self.root)
