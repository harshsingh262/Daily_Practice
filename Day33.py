class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end = " ")
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print("Postorder traversal of binary tree is")
    printPostorder(root)