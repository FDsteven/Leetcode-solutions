
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_binary_tree(root, level=0):
    if not root:
        return
    print("  " * level + str(root.val))
    # print left subtree then right subtree
    print_binary_tree(root.left, level + 1)
    print_binary_tree(root.right, level + 1)

# test
root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3))
print_binary_tree(root)

