class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def print_preorder(root):
    if root:
        print(root.value, end=" ")
        print_preorder(root.left)
        print_preorder(root.right)


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.value, end=" ")
        print_in_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.value, end=" ")


def print_level_order(root):
    # In queue, we add values to the end and remove from the beginning
    if root:  # if root is not None

        # create an empty queue
        queue = []

        # add the root to the queue
        queue.append(root)

        while queue:
            # pop the first element from the queue and print it
            node = queue.pop(0)
            print(node.value, end=" ")

            # enqueue left child
            if node.left:  # if node.left  is not None
                queue.append(node.left)

            # enqueue right child
            if node.right:  # if node.right is not None
                queue.append(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Pre order traversal: ")
    print_preorder(root)

    print("\nIn Order traversal: ")
    print_in_order(root)

    print("\nPost Order traversal: ")
    print_post_order(root)

    print("\nLevel Order Traversal:")
    print_level_order(root)
