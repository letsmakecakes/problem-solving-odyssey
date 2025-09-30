# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists iteratively.
        Time: O(n + m), Space: O(1)
        """
        # Create dummy node to simply edge cases
        dummy = ListNode(0)
        current = dummy

        # Merge nodes while both lists have elements
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes (at most one list is non-empty)
        current.next = list1 if list1 else list2
        
        return dummy.next