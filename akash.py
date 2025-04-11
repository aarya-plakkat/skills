
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def check_all_leaves_at_same_level(root):
    if not root:
        return True
    
    # Initialize a queue for level order traversal (BFS)
    queue = []
    queue.append((root, 0))  # (node, level)
    
    leaf_level = None
    
    while queue:
        node, level = queue.pop(0)
        
        # If it's a leaf node
        if not node.left and not node.right:
            # If it's the first leaf node, store its level
            if leaf_level is None:
                leaf_level = level
            # If the leaf node's level is not the same as the first leaf's level
            elif leaf_level != level:
                return False
        
        # Add left and right children to the queue with incremented level
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return True

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

if check_all_leaves_at_same_level(root):
    print("All leaf nodes are at the same level.")
else:
    print("Leaf nodes are not at the same level.")