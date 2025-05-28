from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Calculate the average value of nodes at each level in a binary tree.

        Args:
            root: The root node of the binary tree
        
        Returns:
            List of floats representing the average value at each level
        """
        if not root:
            return []
        
        queue = deque([root])
        level_averages = []

        while queue:
            level_sum = 0
            level_size = len(queue)

            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate and store the average for this level
            level_average = level_sum / level_size
            level_averages.append(level_average)
        
        return level_averages