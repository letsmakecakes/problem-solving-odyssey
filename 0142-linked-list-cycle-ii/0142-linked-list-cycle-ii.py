# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects and returns the node where the cycle begins in a linked list.
        Uses Floyd's Cycle Detection Algorithm (Tortoise and Hare).
        
        Algorithm:
        1. Phase 1: Use slow/fast pointers to detect if cycle exists
        2. Phase 2: If cycle exists, find the starting node of the cycle
        
        Mathematical insight: 
        When pointers meet, distance from head to cycle start equals 
        distance from meeting point to cycle start.
        
        Args:
            head: The head node of the linked list
            
        Returns:
            Optional[ListNode]: The node where cycle begins, or None if no cycle
            
        Time Complexity: O(n), Space Complexity: O(1)
        """
        # Edge case: empty list or single node
        if not head or not head.next:
            return None
        
        # Phase 1: Detect cycle using two pointers
        slow = fast = head
        
        # Find meeting point (if cycle exists)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            # No cycle found (while loop completed without break)
            return None
        
        # Phase 2: Find cycle start
        # Move one pointer to head, keep other at meeting point
        # They will meet at the cycle start
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow  # This is where the cycle begins
