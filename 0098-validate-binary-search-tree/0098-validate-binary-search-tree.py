# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate if a binary tree is a valid Binary Search Tree.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        self.prev_val = float('-inf')

        def inorder(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            # Check left subtree
            if not inorder(node.left):
                return False
            
            # Check current node against previous value
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val

            # Check right subtree
            return inorder(node.right)
        
        return inorder(root)