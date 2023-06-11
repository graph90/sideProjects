class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
 
class BinarySearchTree:
    def __init__(self):
        self.root = None
 
    def insert(self, key):
        self.root = self.insertRecursive(self.root, key)
 
    def insertRecursive(self, root, key):
        if root is None:
            root = Node(key)
            return root
 
        if key < root.key:
            root.left = self.insertRecursive(root.left, key)
        elif key > root.key:
            root.right = self.insertRecursive(root.right, key)
 
        return root
 
    def search(self, root, key):
        if root is None or root.key == key:
            return root
 
        if key < root.key:
            return self.search(root.left, key)
 
        return self.search(root.right, key)
 
 
# Create a new binary search tree
tree = BinarySearchTree()
 
# Inserting nodes in the binary search tree
tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
 
# Searching for a node with a given key
searchedNode = tree.search(tree.root, 40)
print("Searched node: ", searchedNode.key)
