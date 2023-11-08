class BinarySearchTree:
    def __init__(self, val, left=None, right=None):
        """
        Initialize a new BinarySearchTree node with the given value and left and right.
        arguments:
            val: The value of the node.
            left: The left child of the node.
            right: The right child of the node.
        """
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """
        Return a string representation of the BinarySearchTree node.
        """
        return f"{self.val} ({self.left}, {self.right})"


def get_closest_numbers(tree, f, p):
    """
    Get the p closest numbers to f in the given BinarySearchTree.
    Args:
        tree: The BinarySearchTree to search for closest numbers.
        f: The number to search for closest numbers to.
        p: The number of closest numbers to return.
    Returns:
        A list of the p closest numbers to f in the BinarySearchTree.
    """
    def dfs(node):
        """
        Traverse the BinarySearchTree in-order and append each node's value to the values list.
        Args:
            node: The current node being traversed.
        """
        if not node:
            return
        dfs(node.left)
        values.append(node.val)
        dfs(node.right)

    values = []
    dfs(tree)
    values.sort(key=lambda x: abs(x-f), reverse=True)
    return values[-p:]
