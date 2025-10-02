# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform inorder traversal (;eft -> root -> right) of a binary tree.
        Returns list of node values in inorder sequence.
        """
        result = []
        self._inorder_helper(root, result)
        return result
        
    def _inorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        """Helper method for recursive inorder traversal."""
        if not node:
            return
            
        self._inorder_helper(node.left, result)
        result.append(node.val)
        self._inorder_helper(node.right, result)
        
