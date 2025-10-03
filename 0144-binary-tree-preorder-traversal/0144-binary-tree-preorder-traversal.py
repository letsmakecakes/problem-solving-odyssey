# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs preorder traversal of a binary tree.
        
        Args:
            root: The root node of the binary tree
            
        Returns:
            List of node values in preorder sequence
        """
        result = []
        self._traverse(root, result)
        return result
    
    def _traverse(self, node: Optional[TreeNode], result: List[int]) -> None:
        """Helper method to perform recursive traversal."""
        if node is None:
            return
        
        result.append(node.val)
        self._traverse(node.left, result)
        self._traverse(node.right, result)