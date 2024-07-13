class TreeNode:
    """A node in a binary search tree.

    Attributes:
        key (int): The value stored in the node.
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """

    def __init__(self, key):
        """
        Initializes a TreeNode with the specified key.

        Args:
            key (int): The value to be stored in the node.
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns a string representation of the node's key.

        Returns:
            str: The string representation of the key.
        """
        return str(self.key)


class BinarySearchTree:
    """A binary search tree implementation.

    Attributes:
        root (TreeNode): The root node of the binary search tree.
    
    Examples:
        >>> bst = BinarySearchTree()
        >>> bst.insert(10)
        >>> bst.insert(5)
        >>> bst.insert(15)
        >>> bst.search(10).key
        10
        >>> bst.search(7) is None
        True
        >>> bst.delete(10)
        >>> bst.search(10) is None
        True
        >>> bst.inorder_traversal()
        [5, 15]
    """

    def __init__(self):
        """
        Initializes an empty binary search tree.
        """
        self.root = None

    def _insert(self, node, key):
        """
        Recursively inserts a key into the binary search tree.

        Args:
            node (TreeNode): The current node in the tree.
            key (int): The value to be inserted.

        Returns:
            TreeNode: The node after insertion.
        """
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        """
        Inserts a key into the binary search tree.

        Args:
            key (int): The value to be inserted.
        """
        self.root = self._insert(self.root, key)

    def _search(self, node, key):
        """
        Recursively searches for a key in the binary search tree.

        Args:
            node (TreeNode): The current node in the tree.
            key (int): The value to be searched for.

        Returns:
            TreeNode: The node containing the key, or None if not found.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """
        Searches for a key in the binary search tree.

        Args:
            key (int): The value to be searched for.

        Returns:
            TreeNode: The node containing the key, or None if not found.
        """
        return self._search(self.root, key)

    def _delete(self, node, key):
        """
        Recursively deletes a key from the binary search tree.

        Args:
            node (TreeNode): The current node in the tree.
            key (int): The value to be deleted.

        Returns:
            TreeNode: The node after deletion.
        """
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def delete(self, key):
        """
        Deletes a key from the binary search tree.

        Args:
            key (int): The value to be deleted.
        """
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """
        Finds the minimum value in a subtree.

        Args:
            node (TreeNode): The root node of the subtree.

        Returns:
            int: The minimum value in the subtree.
        """
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        """
        Recursively performs an in-order traversal of the binary search tree.

        Args:
            node (TreeNode): The current node in the tree.
            result (list): The list to store the traversal result.
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the binary search tree.

        Returns:
            list: The list of keys in in-order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)

print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)

print("Search for 40:", bst.search(40))
print("Inorder traversal after deleting 40:",bst.inorder_traversal())