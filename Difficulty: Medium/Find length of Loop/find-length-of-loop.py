'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        """
        Detect if a cycle exists in a linked list and return its length.
        Uses Floyd's Cycle Detection Algorithm (Tortoise and Hare).
        
        Returns:
            int: Length of the loop if it exists, 0 otherwise
        """
        # Phase 1: Detect if a cycle exists
        meeting_point = self._detect_cycle(head)
        if not meeting_point:
            return 0
        
        # Phase 2: Count the loop length
        return self._count_loop_length(meeting_point)
        
    def _detect_cycle(self, head):
        """
        Detect if a cycle exists using two pointers.
        
        Returns:
            Node: The meeting point if cycle exists, None otherwise
        """
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return slow # Return the meeting point
        
        return None # No cycle found
    
    def _count_loop_length(self, meeting_point):
        """
        Count the number of nodes in the loop starting from meeting point.
        
        Args:
            meeting_point: A node in the cycle
        
        Returns:
            int: Length of the loop
        """
        current = meeting_point.next
        length = 1
        
        while current != meeting_point:
            current = current.next
            length += 1
        
        return length