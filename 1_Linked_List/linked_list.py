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
    def __init__(self, value=None):
        """Initialize a linked list with a head node containing the given value.

        Args:
            value: The value for the head node of the linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
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

        # Handle the case when there's only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp.next is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
        
        self.length -= 1
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
            The node at the specified index, or None if the index is invalid.
        """
        if index >= self.length or index < 0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        """Set the value of the node at the specified index.

        Args:
            index: The index of the node whose value is to be set.
            value: The new value to set for the node.

        Returns:
            bool: True if the value is successfully set, False if the index is invalid.
        """
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert a new node with the given value at the specified index.

        Args:
            index: The position where the new node should be inserted.
            value: The value for the new node.

        Returns:
            bool: True if the node is successfully inserted, False if the index is invalid.
        """
        if index > self.length or index < 0:
            return False

        if index == 0:
            self.prepend(value)
            return True

        if index == self.length:
            self.append(value)
            return True

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def remove(self, index):
        """Remove the node at the specified index.

        Args:
            index: The index of the node to be removed.

        Returns:
            The removed node, or None if the index is invalid.
        """
        if index >= self.length or index < 0:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def reverse(self):
        """Reverse the order of nodes in the linked list."""
        if self.length <= 1:  # No need to reverse if list is empty or has only 1 node
            return

        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None

        # Traverse and reverse pointers
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def print_list(self):
        """Print the values of all nodes in the linked list."""
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next
