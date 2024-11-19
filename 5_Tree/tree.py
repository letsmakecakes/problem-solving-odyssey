"""
This module implements a simple binary search tree (BST) with insertion
and search (contains) functionalities. It also includes test cases to
validate the implementation of these operations.

Classes:
    Node: Represents a single node in the binary search tree.
    BinarySearchTree: Implements the binary search tree with insert and contains operations.

Functions:
    check(expect, actual, message): Utility function to compare expected and actual results
    during tests and print the results.
"""


class Node:
    """
    A node in a binary search tree.

    Attributes:
        value: The value stored at the node.
        left: A reference to the left child node.
        right: A reference to the right child node.
    """

    def __init__(self, value):
        """
        Initializes a node with a given value, and sets the left and right child nodes to None.

        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A binary search tree (BST) that supports insertion of unique values
    and checking if a value exists in the tree.

    Attributes:
        root: The root node of the tree.
    """

    def __init__(self):
        """
        Initializes an empty binary search tree with no root node.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a new value into the binary search tree.
        Values greater than the current node go to the right, and
        values smaller go to the left. Duplicate values are not inserted.

        Args:
            value: The value to insert into the tree.

        Returns:
            bool: True if the value was successfully inserted, False if the value
                  already exists in the tree.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    break
                else:
                    temp = temp.right
            else:
                if temp.left is None:
                    temp.left = new_node
                    break
                else:
                    temp = temp.left

        return True

    def contains(self, value):
        """
        Checks if a value exists in the binary search tree.

        Args:
            value: The value to search for in the tree.

        Returns:
            bool: True if the value exists in the tree, False otherwise.
        """
        temp = self.root
        while temp is not None:
            if value > temp.value:
                temp = temp.right
            elif value < temp.value:
                temp = temp.left
            else:
                return True

        return False

    def __r_contains(self, current_node, value):
        """
        Recursively checks if a value exists in the binary search tree.

        Args:
            current_node (Node): The current node being checked.
            value: The value to search for.

        Returns:
            bool: True if the value exists, False otherwise.
        """
        if current_node is None:
            return False

        if current_node.value == value:
            return True

        if value < current_node.value:
            return self.__r_contains(current_node.left, value)

        return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        """
        Public method to initiate a recursive search for a value in the tree.

        Args:
            value: The value to search for.

        Returns:
            bool: True if the value exists, False otherwise.
        """
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        """
        Recursively inserts a value into the binary search tree.

        Args:
            current_node (Node): The current node being checked.
            value: The value to insert.

        Returns:
            Node: The current node after insertion.
        """
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        """
        Public method to initiate recursive insertion of a value into the tree.

        Args:
            value: The value to insert into the tree.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)