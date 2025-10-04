# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: empty list
        if not head:
            return None
        
        # Edge case: single node list should return None
        if not head.next:
            return None

        # Use two pointers: slow moves 1 step, fast moves 2 steps
        # When fast reaches the end, slow will be just before the middle
        slow = head
        fast = head.next.next

        # Traverse until fast reaches the end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node by skipping it
        slow.next = slow.next.next

        return head