from collections import deque

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        if not root:
            return []
            
        queue = deque([(root, 0)])
        top_view_map = {}
    
        
        while queue:
            node, hd = queue.popleft()
            
            # Only store the first node encountered at each horizontal distance
            if hd not in top_view_map:
                top_view_map[hd] = node.data
            
            # Add children to queue with updated horizontal distances
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        return [top_view_map[hd] for hd in sorted(top_view_map.keys())]