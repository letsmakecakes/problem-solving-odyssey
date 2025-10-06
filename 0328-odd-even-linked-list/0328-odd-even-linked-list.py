# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Rearranges a linked list so all odd-indexed nodes comes before even-indexed nodes.

        Args:
            head: The head of the singly-linked list
        
        Returns:
            The head of the rearranged list
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using pointers
        """
        # Handle edge cases: empty list or single node
        if not head or not head.next:
            return head
        
        # Initialize pointers for odd and even chains
        odd_ptr = head
        even_ptr = head.next
        even_head = even_ptr # Save the head of even chain to connect later

        # Traverse and separate odd/even nodes
        while even_ptr and even_ptr.next:
            # Link current odd node to next odd node
            odd_ptr.next = even_ptr.next
            odd_ptr = odd_ptr.next

            # Link current even node to next even node
            even_ptr.next = odd_ptr.next
            even_ptr = even_ptr.next
        
        # Connect the end of odd chain to the start of even chain
        odd_ptr.next = even_head

        return head