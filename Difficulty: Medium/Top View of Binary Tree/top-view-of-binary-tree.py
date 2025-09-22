from collections import deque
# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        """
        Returns the top view of a binary tree using BFS and horizontal distance mapping.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the width of the tree
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of integers representing the top view from left to right
        """
        if not root:
            return []
        
        hd_map: Dict[int, Node] = {}
        queue = deque([(root, 0)])
        min_hd = max_hd = 0
        
        while queue:
            node, hd = queue.popleft()
            
            # Track min and max horizontal distances
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            # Store first node at this horizontal distance
            if hd not in hd_map:
                hd_map[hd] = node
            
            # Add children
            if node.left:
                queue.append((node.left, hd -1))
            if node.right:
                queue.append((node.right, hd +1))
        
        # Build result using range from min to max horizontal distance
        return [hd_map[hd].data for hd in range(min_hd, max_hd + 1)]