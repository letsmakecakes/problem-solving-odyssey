# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Find intersection node of two linked lists using hash set approach.
        Time: O(m + n), Space: O(1) where m, n are lengths of lists.

        Key insight: When pointer reaches end, redirect to other list's head.
        Both pointers will travel same total distance and meet at intersection.
        """
        if not headA or not headB:
            return None
        
        pointerA, pointerB = headA, headB

        # Traverse until pointers meet (or both become None)
        while pointerA != pointerB:
            # When reaching end, switch to other list's head
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        
        return pointerA # Either intersection node or None