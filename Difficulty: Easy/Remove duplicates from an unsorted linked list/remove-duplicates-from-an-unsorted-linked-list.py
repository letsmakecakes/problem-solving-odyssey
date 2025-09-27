'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        """
        Remove duplicates form an unsorted singly linked list.
        Keeps the first occurence of each value.
        
        Args:
            head: Head node of the unsorted linked list
        
        Returns:
            Node: Head of the modified linked list
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for the set to store unique values
        """
        if not head:
            return head
        
        seen_values = set()
        seen_values.add(head.data) # Add first node's data
        current = head
        
        # Process remaining nodes
        while current.next:
            if current.next.data in seen_values:
                # Remove duplicate node by skipping it
                current.next = current.next.next
            else:
                # First occurence - keep it and move forward
                seen_values.add(current.next.data)
                current = current.next
        
        return head