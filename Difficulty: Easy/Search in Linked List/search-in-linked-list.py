'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):
        """
        Search for a key in a singly-linked list.
        
        Performs linear search through the linked list, checking each node's
        data value until the key is found or the end is reached.
        
        Args:
            head: Head node of the linked list (can be None for empty list)
            key: Value to search for in the list
            
        Returns:
            True if key exists in the list, False otherwise
            
        Examples:
            >>> head = Node(1)
            >>> head.next = Node(2)
            >>> head.next.next = Node(3)
            >>> searchKey(head, 2)
            True
            >>> searchKey(head, 5)
            False
            >>> searchKey(None, 1)
            False
        """
        current = head
        
        while current:
            if current.data == key:
                return True
            current = current.next
        
        return False