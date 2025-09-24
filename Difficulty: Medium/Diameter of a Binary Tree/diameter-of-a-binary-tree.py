'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def diameter(self, root):
        """
        Calculate the diameter of a binary tree (longest path between any two nodes).
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root node of the binary tree
        
        Returns:
            The diameter of the tree (number of edges in the longest path)
        """
        self.max_diameter = 0
        
        def calculate_height(node) -> int:
            """
            Calculate height of subtree and update max diameter.
            
            Returns:
                Height of the current subtree
            """
            if not node:
                return 0
            
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            
            # Update max diameter: path through current node
            current_diameter = left_height + right_height
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return height of current subtree
            return 1 + max(left_height, right_height)
            
        calculate_height(root)
        return self.max_diameter
        