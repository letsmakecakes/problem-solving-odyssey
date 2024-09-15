"""
This module provides an implementation of a stack using a singly linked list.
The stack supports basic operations such as push, pop, and print.
"""

class Node:
    """
    A Node in a singly linked list.
    
    Attributes:
        value: The value stored in the node.
        next: A pointer to the next node in the list, or None if there is no next node.
    """
    def __init__(self, value):
        """
        Initialize a new node with a given value.
        
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.next = None


class Stack:
    """
    A Stack data structure implemented using a singly linked list.
    
    Attributes:
        top: The top node of the stack.
        height: The number of elements in the stack.
    """
    def __init__(self, value):
        """
        Initialize a new stack with a given value as the first element.
        
        Args:
            value: The initial value to be stored in the stack.
        """
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        """
        Push a new value onto the top of the stack.
        
        Args:
            value: The value to be added to the stack.
        
        Returns:
            True to indicate that the value was successfully pushed onto the stack.
        """
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1

        return True

    def pop(self):
        """
        Remove and return the value at the top of the stack.
        
        Returns:
            The node that was removed from the top of the stack, or None if the stack is empty.
        """
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1

        return temp

    def print_stack(self):
        """
        Print all the values in the stack from top to bottom.
        """
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
