from collections import deque

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def LeftView(self, root):
        """
        Returns the left view of a binary tree using BFS approach.
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) here w is the maximum width of the tree
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
                
                # The first node at each level is the leftmost
                if i == 0:
                    result.append(node.data)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result