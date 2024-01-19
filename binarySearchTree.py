import argparse
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)

    def insert_recursive(self, root, key):
        if root is None:
            root = Node(key)
            return root
        if key < root.key:
            root.left = self.insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self.insert_recursive(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

def main():
    parser = argparse.ArgumentParser(description="Binary Search Tree CLI")
    parser.add_argument("--insert", type=int, help="Insert a key into the binary search tree")
    parser.add_argument("--search", type=int, help="Search for a key in the binary search tree")
    args = parser.parse_args()
    tree = BinarySearchTree()
    if args.insert:
        tree.insert(args.insert)
        print(f"Inserted node with key {args.insert} into the tree.")

    if args.search:
        searched_node = tree.search(tree.root, args.search)
        if searched_node:
            print(f"Searched node: {searched_node.key}")
        else:
            print(f"Node with key {args.search} not found in the tree.")
if __name__ == "__main__":
    main()
