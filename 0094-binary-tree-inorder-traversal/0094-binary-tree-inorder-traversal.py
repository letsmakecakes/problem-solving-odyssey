# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal of a binary tree iteratively.

        Args:
            root: Root node of the binary tree
        
        Returns:
            List of node values in inorder traversal order

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree
        """
        result = []
        stack = []
        current = root

        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node and move to the right subtree
            current = stack.pop()
            result.append(current.val)
            current = current.right
        
        return result