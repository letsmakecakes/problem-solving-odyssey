from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the right side view of a binary tree using BFS approach.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            # Process all nodes at the current level
            for i in range(level_size):
                node = queue.popleft()

                # The last node at each level is the rightmost
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result