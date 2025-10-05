# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees have the same leaf value sequence.

        Args:
            root1: Root of first binary tree
            root2: Root of second binary tree
        
        Returns:
            True if both trees have the same leaf sequence, False otherwise
        """
        return self._get_leaves(root1) == self._get_leaves(root2)

    
    def _get_leaves(self, node: Optional[TreeNode]) -> List[int]:
        """
        Get the leafe values of a binary tree in left-to-right order.

        Args:
            node: Root node of the tree

        Returns:
            List of leaf values
        """
        if not node:
            return []
        
        # If it's a leaf node, return its value
        if not node.left and not node.right:
            return [node.val]
        
        # Recursively get leaves from left and right subtrees
        return self._get_leaves(node.left) + self._get_leaves(node.right)
    