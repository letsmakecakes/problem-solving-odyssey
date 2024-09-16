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
