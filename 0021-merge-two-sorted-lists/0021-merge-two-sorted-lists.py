# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            # Create a dummy node to serve as the starting point of the merged list
            dummy = ListNode(0)
            current = dummy

            # Traverse both lists and merge them
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            
            # Attach the remaining nodes from either list1 or list2
            current.next = list1 if list1 else list2

            # Return the merged list, starting from the node after the dummy node.
            return dummy.next