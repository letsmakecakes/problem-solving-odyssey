from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        Performs level-order traversal of an N-ary tree.

        Args:
            root: The root node of the N-ary tree
        
        Returns:
            A list of lists containing node values level by level from top to bottom
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

                # Add all children to queue for next level
                queue.extend(node.children)
                
            levels.append(current_level)
        
        return levels