# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Convert binary linked list to decimal using bit shifting (most efficient).

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(1)
        """
        if not head:
            return 0
        
        result = 0
        current = head

        while current:
            # Left shift result by 1 bit and add current bit
            result = (result << 1) + current.val
            current = current.next
        
        return result