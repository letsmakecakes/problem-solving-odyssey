'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        """
        Removes loop from linked list using Floyd's Cycle Detection Algorithm.
        
        Args:
            head: Head node of the linked list
            
        Returns:
            None (modifies the list in-place)
        """
        # Edge case: empty list
        if not head or not head.next:
            return
        
        # Phase 1: Detect if loop exists using slow and fast pointers
        slow = fast = head
        loop_detected = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                loop_detected = True
                break
        
        # If no loop found, return early
        if not loop_detected:
            return
        
        # Phase 2: Find the start of the loop
        # Reset slow pointer to head, keep fast at meeting point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Phase 3: Find the node just before the loop start and break the loop
        # At this point, both slow and fast are at the loop start
        while fast.next != slow:
            fast = fast.next
        
        # Break the loop
        fast.next = None