from collections import deque

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        """
        Returns the bottom view of a binary tree using level-order traversal
        with horizontal distance tracking.
        
        The bottom view consists of nodes visible when viewing the tree from below.
        For each horizontal distance, the last node encountered during level-order
        traversal is part of the bottom view.
        
        Args:
            root: The root node of the binary tree
            
        Returns:
            List of node values representing the bottom view from left to right
        """
        # Handle edge case: empty tree
        if not root:
            return []
        
        # Queue stores tuples of (node, horizontal_distance)
        queue = deque([(root, 0)])
        bottom_view = {}
        min_hd = 0
        max_hd = 0
        
        while queue:
            node, hd = queue.popleft()
            
            # Track the range of horizontal distances
            min_hd = min(hd, min_hd)
            max_hd = max(hd, max_hd)
            
            # Update bottom view - last node at each horizontal distance wins
            bottom_view[hd] = node.data
            
            # Add children with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Build result from left to right using horizontal distance range
        return [bottom_view[hd] for hd in range(min_hd, max_hd + 1)]