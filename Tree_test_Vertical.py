'''
This is broken, don't use this please
'''

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def get_height(node):
    if node is None:
        return 0
    return max(get_height(node.left), get_height(node.right)) + 1

def print_tree_vertically(root):
    def print_level(node, level, distance):
        if node:
            if level == 1:
                print(' ' * (distance - node_width // 2) + str(node.value), end='')
            else:
                print_level(node.left, level - 1, distance - level_width)
                print_level(node.right, level - 1, distance + level_width)

    height = get_height(root)
    level_width = 4  # Width between levels
    node_width = 3   # Width of each node value
    for i in range(1, height + 1):
        print_level(root, i, (2 ** height - 1) * level_width)
        print()  # Move to the next line for the next level

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

# Print the binary tree vertically
print("\nVertical Binary Tree:")
print_tree_vertically(tree)
