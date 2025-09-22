from collections import deque

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        """
        Returns the bottom view of a binary tree using BFS and horizontal distance mapping.
        
        The bottom view consists of nodes that are visible when the tree is viewed from below.
        We use horizontal distance (HD) to track position relative to root:
        - Root has HD = 0
        - Left child has HD = parent_HD - 1  
        - Right child has HD = parent_HD + 1
        
        Unlike top view, we keep updating nodes at each HD to get the bottommost node.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for queue and hashmap storage
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of integers representing the bottom view from left to right
        """
        if not root:
            return []
        
        # Map to store the bottommost node at each horizontal distance
        hd_map: Dict[int, Node] = {}
        
        # BFS queue storing (node, horizontal_distance) pairs
        queue = deque([(root, 0)])
        min_hd = max_hd = 0
        
        while queue:
            node, horizontal_distance = queue.popleft()
            
            # Always update the node at this horizontal distance
            # (later nodes in BFS will be at lower levels, hence "bottom")
            hd_map[horizontal_distance] = node
            
            # Track the range of horizontal distances
            min_hd = min(min_hd, horizontal_distance)
            max_hd = max(max_hd, horizontal_distance)
            
            # Add children with updated horizontal distances
            if node.left:
                queue.append((node.left, horizontal_distance - 1))
            if node.right:
                queue.append((node.right, horizontal_distance + 1))
        
        # Build result using range from min to max horizontal distance
        return [hd_map[hd].data for hd in range(min_hd, max_hd + 1)]