from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        BFS approach - processes level by level without tracking individual depths.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            depth += 1
            level_size = len(queue)

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()

                # Add children for next level
                for child in (node.left, node.right):
                    if child:
                        queue.append(child)
        
        return depth