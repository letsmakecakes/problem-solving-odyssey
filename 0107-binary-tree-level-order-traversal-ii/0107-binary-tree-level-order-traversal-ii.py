from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level-order traversal of a binary tree from bottom to top.

        Args:
            root: The root node of the binary tree
        
        Returns:
            A list of lists containing node values level by level from bottom to top
        """
        if not root:
            return []
        
        queue = deque([root])
        levels = []

        while queue:
            current_level = []
            level_size = len(queue)

            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(current_level)
        
        # Reverse to get bottom-up order
        return levels[::-1]