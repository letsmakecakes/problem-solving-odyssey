"""
This module implements a doubly linked list data structure.

Classes:
    Node: Represents a node in a doubly linked list.
    DoublyLinkedList: Represents a doubly linked list.
"""


class Node:
    """
    Represents a node in a doubly linked list.

    Attributes:
        value: The value stored in the node.
        prev: A reference to the previous node in the list.
        next: A reference to the next node in the list.
    """

    def __init__(self, value):
        """
        Initializes a new node with the given value.

        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """
    Represents a doubly linked list.

    Attributes:
        head: The first node in the list.
        tail: The last node in the list.
        length: The number of nodes in the list.
    """

    def __init__(self, value):
        """
        Initializes a new doubly linked list with a single node.

        Args:
            value: The value of the initial node.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value) -> bool:
        """
        Adds a new node with the given value to the end of the list.

        Args:
            value: The value to append to the list.

        Returns:
            True if the node is appended successfully.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True

    def pop(self) -> Node:
        """
        Removes and returns the last node in the list.

        Returns:
            The removed node, or None if the list is empty.
        """
        if self.head is None:
            return None

        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None

        self.length -= 1

        return temp

    def prepend(self, value) -> bool:
        """
        Adds a new node with the given value to the start of the list.

        Args:
            value: The value to prepend to the list.

        Returns:
            True if the node is prepended successfully.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True

    def pop_first(self) -> Node:
        """
        Removes and returns the first node in the list.

        Returns:
            The removed node, or None if the list is empty.
        """
        if self.head is None:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None

        self.length -= 1

        return temp

    def get(self, index) -> Node:
        """
        Retrieves the node at the specified index.

        Args:
            index: The index of the node to retrieve.

        Returns:
            The node at the specified index, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None

        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev

        return temp

    def set_value(self, index, value) -> bool:
        """
        Updates the value of the node at the specified index.

        Args:
            index: The index of the node to update.
            value: The new value to set.

        Returns:
            True if the value is updated successfully, False if the index is out of range.
        """
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True

        return False

    def insert(self, index, value) -> bool:
        """
        Inserts a new node with the given value at the specified index.

        Args:
            index: The index at which to insert the new node.
            value: The value of the new node.

        Returns:
            True if the node is inserted successfully, False if the index is out of range.
        """
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1

        return True

    def remove(self, index) -> Node:
        """
        Removes and returns the node at the specified index.

        Args:
            index: The index of the node to remove.

        Returns:
            The removed node, or None if the index is out of range.
        """
        if index < 0 or index >= self.length:
            return None

        if index == self.length - 1:
            return self.pop()

        if index == 0:
            return self.pop_first()

        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1

        return temp

    def print_list(self):
        """
        Prints the values of all nodes in the list.
        """
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
