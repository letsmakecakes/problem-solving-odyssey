from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs bottom-up level order traversal of a binary tree.

        Args:
            root: The root node of the binary tree
        
        Returns:
            A list of lits containing node values level by level from bottom to top

        Time Complexity: O(1) using deque prepend operations
        Space Complexity: O(w) where w is the maximum width of the tree
        """
        if not root:
            return []
        
        queue = deque([root])
        result = deque()

        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.appendleft(current_level)
        
        return list(result)