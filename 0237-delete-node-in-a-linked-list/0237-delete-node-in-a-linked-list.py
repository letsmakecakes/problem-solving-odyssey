# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        Delete a node from a singly-linked list given only access to that node.
        
        This is a "trick" problem: we can't actually delete the node since we
        don't have access to the previous node. Instead, we copy the next node's
        value into the current node and skip over the next node.
        
        Constraints (guaranteed by problem):
        - The node to be deleted is NOT the tail of the list
        - The node to be deleted is a valid node in the list
        
        Args:
            node: The node to be "deleted" (modified in-place)
            
        Returns:
            None (modifies the linked list in-place)
            
        Example:
            Input:  1 -> 2 -> 3 -> 4, node = 3
            After:  1 -> 2 -> 4
            (We copy 4's value to node 3, then skip node 4)
        """
        # Copy the next node's value into current node
        node.val = node.next.val
        
        # Skip over the next node (effectively "deleting" it)
        node.next = node.next.next