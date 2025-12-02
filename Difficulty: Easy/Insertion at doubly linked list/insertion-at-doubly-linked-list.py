'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''

class Solution:
    def insertAtPos(self, head, p, x):
        # Create new node
        new_node = Node(x)
        
        # Navigate to the p-th node
        current = head
        for _ in range(p):
            if not current: # Handle out of bounds
                return head
            current = current.next
        
        # Handle edge cases: current is None (poistion out of bounds)
        if not current:
            return head
            
        # Insert new_node after current
        new_node.next = current.next
        new_node.prev = current
        
        if current.next: # Update next node's prev pointer if it exists
            current.next.prev = new_node
        
        current.next = new_node
        
        return head