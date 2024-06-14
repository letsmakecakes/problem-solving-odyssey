'''This module defines a basic singly linked list data structure.

The module includes:
- A `Node` class representing an element in the linked list.
- A `LinkedList` class providing methods to manipulate the linked list.
'''


class Node:
    """A class representing a node in a linked list."""

    def __init__(self, value):
        """Initialize a node with a given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:
    """A class representing a linked list."""

    def __init__(self, value):
        """Initialize a linked list with a head node containing the given value.

        Args:
            value: The value for the head node of the linked list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """Append a new node with the given value to the end of the linked list.

        Args:
            value: The value to be appended to the list.

        Returns:
            bool: True if the node is successfully appended.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True

    def prepend(self, value):
        """Prepend a new node with the given value to the beginning of the linked list.

        Args:
            value: The value to be prepended to the list.

        Returns:
            bool: True if the node is successfully prepended.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True

    def pop(self):
        """Remove and return the last node from the linked list.

        Returns:
            The value of the removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value

    def pop_first(self):
        """Remove and return the first node from the linked list.

        Returns:
            The value of the removed node, or None if the list is empty.
        """
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp.value

    def get(self, index):
        """Get the value of the node at the specified index.

        Args:
            index: The index of the node whose value is to be retrieved.

        Returns:
            The value of the node at the specified index, or None if the index is out of bounds or the list is empty.
        """
        if self.length == 0:
            return None

        if index >= self.length:
            return None

        temp = self.head
        for _ in range(0, index):
            temp = temp.next

        return temp.value

    def print_list(self):
        """Print the values of all nodes in the linked list."""
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(3)
my_linked_list.print_list()

print("value at index 1", my_linked_list.get(1))
