# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Swaps the values of the kth node from the beginning and kth node from the end.

        Args:
            head: Head of the linked list
            k: Position from beginning/end (1-indexed)
        
        Returns:
            Head of the modified linked list
        
        Time Complexity: O(n) - single pass through the list
        Space Complexity: O(1) - only using pointers
        """
        if not head or k <= 0:
            return head
        
        # Find the kth node from the beginning
        kth_from_start = self._find_kth_from_start(head, k)
        if not kth_from_start:
            return head # k is larger than the list length
        
        # Find the kth node from the end using two pointer technique
        kth_from_end = self._find_kth_from_end(head, kth_from_start, k)

        # Swap the values
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

        return head
    
    def _find_kth_from_start(self, head: ListNode, k: int) -> Optional[ListNode]:
        """Find the kth node from the beggining (1-indexed)."""
        current = head
        for _ in range(k - 1):
            if not current:
                return None
            current = current.next
        
        return current
    
    def _find_kth_from_end(self, head: ListNode, kth_from_start: ListNode, k: int) -> ListNode:
        """
        Find the kth node from the end using two-pointer technique.

        The kth_from_start pointer is already k positions ahead, 
        so when it reaches the end, the slow pointer will be at the kth from end.
        """
        kth_from_end = head
        current = kth_from_start

        # Move both pointers until current reaches the end
        while current.next:
            current = current.next
            kth_from_end = kth_from_end.next

        return kth_from_end