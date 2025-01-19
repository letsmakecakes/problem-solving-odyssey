# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        group_previous = dummy_node

        while True:
            kthNode = self.__getKthNode(group_previous, k)
            if not kthNode:
                break

            group_next = kthNode.next
            previous, current = kthNode.next, group_previous.next
            while current != group_next:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            
            new_previous = group_previous.next
            group_previous.next = kthNode
            group_previous = new_previous
        
        return dummy_node.next
    
    def __getKthNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current