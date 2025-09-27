from collections import deque

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def rightView(self,root):
        """
        Returns the right view of a binary tree using level-order traversal.
        
        The right view consists of the rightmost node at each level when
        looking at the tree from the right side.
        
        Args:
            root: The root node of the binary tree
            
        Returns:
            List of values representing the right view of the tree
            
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return []
        
        queue = deque([root])
        right_view = []
        
        while queue:
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.popleft()
                
                # The last node at each level is part of the right view
                if i == level_size - 1:
                    right_view.append(node.data)
                
                # Add children to queue for next level (left first, then right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view