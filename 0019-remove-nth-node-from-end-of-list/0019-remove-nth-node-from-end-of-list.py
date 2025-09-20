# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use dummy node to handle edge case of removing head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        fast = slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
            
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next