"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        """
        Reverses a doubly linked list by swapping next and prev pointers.
        
        Args:
            head: The head node of the doubly linked list
            
        Returns:
            The new head of the reversed list
        """
        if not head:
            return None
        
        current = head
        new_head = None
        
        # Traverse and swap next and prev pointers for each node
        while current:
            # Swap next and prev pointers
            current.next, current.prev = current.prev, current.next
            
            # Move to the next node (which is now in prev due to swap)
            new_head = current
            current = current.prev
        
        return new_head
        