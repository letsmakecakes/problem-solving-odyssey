# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty, there is no cycle
        if not head:
            return False
        
        # Initialize two pointers
        fast_ptr = head
        slow_ptr = head

        # Traverse the list with two pointers
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next # Move fast_ptr two steps
            slow_ptr = slow_ptr.next      # Move slow_ptr one step

            # Check if the two pointers meet
            if fast_ptr == slow_ptr:
                return True
        
        # If we reach here, there is no cycle
        return False