# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Delete a node from a singly-linked list given only acces to that node.
        Note: The node to delete is guaranteed not to be tail node.

        Strategy: Copy the next node's value and skip the next node.
        """
        # Copy next node's value to current node
        node.val = node.next.val

        # Skip the next node (effectively deleting it)
        node.next = node.next.next