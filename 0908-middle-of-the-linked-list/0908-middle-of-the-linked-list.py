# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty, return None
        if not head:
            return None
        
        # Initialize two pointers. Fast pointer moves two steps at a time, slow pointer moves one step.
        fast_ptr = head
        slow_ptr = head

        # Traverse the list
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow_ptr