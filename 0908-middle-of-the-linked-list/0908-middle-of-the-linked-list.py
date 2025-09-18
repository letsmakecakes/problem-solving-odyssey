# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a linked list using the two-pointer technique.

        For lists with even length, returns the second middle node.
        Time complexity: O(n), Space complexity: O(1)

        Args:
            head: The head of the singly-linked list

        Returns:
            The middle node of the list, or None if list is empty
        """
        # Handle edge cases: empty list
        if not head:
            return head
        
        # Initialize both pointers to head
        slow = fast = head

        # Move slow pointer one step and fast pointer two steps
        # When fast reaches the end, slow will be at the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow