from BST import BST


class ST:
    def __init__(self):
        self.tree = BST()

    def add(self, symbol):
        return self.tree.insert(symbol)

    def print(self):
        return self.tree.print()
