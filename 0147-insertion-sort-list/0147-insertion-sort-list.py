# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Sort a linked list using insertion sort algorithm.

        Args:
            head: Head of the linked list
        
        Returns:
            Head of the sorted linked list
        """
        # Handle edge cases: empty list or single node list
        if not head or not head.next:
            return head
        
        # Create a dummy node to simplify insertion at the begginning
        dummy = ListNode(float('inf')) # Using -infinity ensures proper sorting with any values
        sorted_tail = dummy # Keep track of the tail of sorted portion for optimization

        current = head 

        while current:
            # If current node's value is greater than the tail value,
            # we can simply append it to the end (optimization)
            if current.val >= sorted_tail.val:
                sorted_tail.next = current
                sorted_tail =current
                current = current.next
                sorted_tail.next = None # Cut off the link to the next unsorted node
            else:
                # Need to find the correct position to insert
                next_node = current.next # Save the next node

                # Find the insertion position
                prev = dummy
                while prev.next and prev.next.val < current.val:
                    prev = prev.next
                
                # Insert the current node
                current.next = prev.next
                prev.next = current

                # Move to the next unsorted node
                current = next_node
        
        return dummy.next