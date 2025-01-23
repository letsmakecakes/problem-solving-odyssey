# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = [root] # Initialize the queue with the root node

        while queue:
            level = [] # To store the values of nodes at the current level
            for _ in range(len(queue)): # Process all nodes in the current level
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left) # Add left child to the queue
                if node.right:
                    queue.append(node.right) # Add right child to the queue
            result.append(level) # Add current level to the result
        
        return result