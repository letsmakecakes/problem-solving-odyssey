# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists (digits in reverse order).
        Time: O(max(n, m)), Space: O(max(n, m))
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry, digit = divmod(total, 10)

            current.next = ListNode(digit)
            current = current.next

            # Advance pointers in one line
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next