# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Remove all nodes with value equal to val from the linked list.

        Args:
            head: The head of the linked list
            val: The value to be removed
        
        Returns:
            Optional[ListNode]: Head of the modified linked list
        """
        # Handle empty list case
        if head is None:
            return None
        
        # Create a dummy node to handle potential removal of head
        dummy = ListNode(0)
        dummy.next = head

        # Use a single pointer to traverse the list
        current = dummy

        while current.next:
            if current.next.val == val:
                # Remove the node
                current.next = current.next.next
            else:
                # Move to next node
                current = current.next
        
        return dummy.next