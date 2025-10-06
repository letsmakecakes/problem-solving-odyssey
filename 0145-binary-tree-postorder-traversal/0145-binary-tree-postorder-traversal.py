# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs postoder traversal (Left -> Right -> Root) on a binary tree.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height (recursion stack)
        """
        result = []
        self._postorder_helper(root, result)
        return result


    def _postorder_helper(self, node: Optional[TreeNode], result: List[int]) -> None:
        """Helper function for recursive postorder traversal."""
        if not node:
            return

        self._postorder_helper(node.left, result)
        self._postorder_helper(node.right, result)
        result.append(node.val)