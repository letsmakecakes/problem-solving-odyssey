"""
This module implements a basic Queue data structure using a singly linked list.
The Queue supports standard operations such as enqueue, dequeue, and printing the queue.
"""

class Node:
    """
    A Node in a singly linked list.
    
    Attributes:
        value: The value stored in the node.
        next: A reference to the next node in the list.
    """
    def __init__(self, value):
        """
        Initialize a new node with a given value.
        
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.next = None


class Queue:
    """
    A Queue implemented using a singly linked list. Supports operations
    for adding elements to the end and removing elements from the front.
    
    Attributes:
        first: The first node in the queue.
        last: The last node in the queue.
        length: The current number of elements in the queue.
    """
    def __init__(self, value):
        """
        Initialize a new Queue with a single element.
        
        Args:
            value: The initial value to add to the queue.
        """
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        """
        Add a new element to the end of the queue.
        
        Args:
            value: The value to add to the queue.
        
        Returns:
            bool: True if the element was successfully added.
        """
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

        return True

    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        
        Returns:
            Node: The node removed from the queue, or None if the queue is empty.
        """
        if not self.first:
            return None

        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.last = None

        return temp

    def print_queue(self):
        """
        Print all elements in the queue from front to back.
        """
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
