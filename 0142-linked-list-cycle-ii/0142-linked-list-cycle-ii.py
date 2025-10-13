# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Phase 1: Detect if cycle exists using Floyd's algorithm
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                # Phase 2: Find cycle entry point
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        
        # No cycle detected
        return None