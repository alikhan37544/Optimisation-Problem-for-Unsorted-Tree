class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.weight = 0

    def __str__(self):
        return f"Node({self.value}, Weight: {self.weight})"

def insert_left(node, value):
    if node.left is None:
        node.left = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.left = node.left
        node.left = new_node

def insert_right(node, value):
    if node.right is None:
        node.right = BinaryTree(value)
    else:
        new_node = BinaryTree(value)
        new_node.right = node.right
        node.right = new_node

def print_tree(node, level=0, side=''):
    if node is not None:
        print_tree(node.right, level + 1, 'R')
        print('   ' * level + ' ' * (level > 0) + f"{node.value} ({side}) - Weight: {node.weight}")
        print_tree(node.left, level + 1, 'L')

def build_tree():
    root_value = int(input("Enter the value for the root node: "))
    root = BinaryTree(root_value)
    nodes_to_process = [root]
    while nodes_to_process:
        current_node = nodes_to_process.pop(0)
        left_value = input(f"Enter the value for the left child of {current_node.value} (or leave blank for no left child): ")
        if left_value.strip():
            insert_left(current_node, int(left_value))
            nodes_to_process.append(current_node.left)
        right_value = input(f"Enter the value for the right child of {current_node.value} (or leave blank for no right child): ")
        if right_value.strip():
            insert_right(current_node, int(right_value))
            nodes_to_process.append(current_node.right)
    return root

# Build the binary tree
tree = build_tree()

# Print the binary tree
print("\nBinary Tree:")
print_tree(tree)
