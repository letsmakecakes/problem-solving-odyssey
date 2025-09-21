from collections import deque
'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def mirror(self, root):
        """
        BFS approach
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            # Swap children    
            node.left, node.right = node.right, node.left
            
            # Add children to queue for processing (order doesn't matter after swap)
            for child in (node.left, node.right):
                if child:
                    queue.append(child)
        
        return root