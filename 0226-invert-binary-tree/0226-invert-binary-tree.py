from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree using iterative BFS approach.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree

        Args:
            root: The root of the binary tree to invert

        Returns:
            The root of the inverted binary tree
        """
        if not root:
            return None
        
        queue = deque([root])

        while queue:
            current = queue.popleft()

            # Swap left and right children
            current.left, current.right = current.right, current.left

            # Add non-null children to queue for processing
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
        
        return root