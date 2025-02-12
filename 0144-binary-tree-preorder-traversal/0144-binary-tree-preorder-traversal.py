# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform preorder traversal of a binary tree using iterative approach.
        Visits nodes in Root -> Left -> Right order.

        Args:
            root: Root node of the binary tree
        
        Returns:
            List of node values in preorder traversal order
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree
        """
        if not root:
            return []
        
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right child first (so left child is processed first)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result