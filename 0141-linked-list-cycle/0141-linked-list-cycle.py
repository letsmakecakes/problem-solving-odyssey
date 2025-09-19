# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects if a linked list contains a cycle using Floyd's algorithm.
        
        Uses two pointers moving at different speeds - if there's a cycle,
        they will eventually meet.
        
        Args:
            head: The head node of the linked list
            
        Returns:
            True if the list contains a cycle, False otherwise
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False