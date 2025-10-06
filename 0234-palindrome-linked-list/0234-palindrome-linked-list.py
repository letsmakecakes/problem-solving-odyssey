# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Checks if a linked list a palindrome using O(1) space.

        Strategy:
        1. Find the middle of the list using slow/fast pointers.
        2. Reverse the second half of the list
        3. Compare the first hald with the reversed second half

        Args:
            head: Head of the singly-linked list

        Returns:
            True if the list is a palindrome, False otherwise
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1) - only using pointers
        """
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Step 2: Handle odd-length lists (skip middle element)
        # If fast is not None, the list had odd length
        if fast:
            slow = slow.next
        
        # Step 3: Reverse the second half of the list
        second_half = self._reverse_list(slow)
        
        # Step 4: Compare first half with reversed second half
        fast_half = head
        while second_half:
            if fast_half.val != second_half.val:
                return False
            fast_half = fast_half.next
            second_half = second_half.next

        return True
        

    def _reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a linked list iteratively.

        Args:
            head: Head of the list to reverse
        
        Returns:
            New head of the reversed list
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev