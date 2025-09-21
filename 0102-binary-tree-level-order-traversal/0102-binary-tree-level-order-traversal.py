from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs leve-order traversal of a binary tree.

        Args:
            root: The root node of the binary tree
        
        Returns:
            A list of lits where each inner list contains values at that level
        """
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level = []

            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result