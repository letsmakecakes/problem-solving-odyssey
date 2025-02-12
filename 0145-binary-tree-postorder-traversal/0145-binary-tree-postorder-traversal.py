# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform postorder traversal iteratively (Left -> Right -> Root).
        Uses a single stack with last visited tracking.

        Time: O(n) where n is number of nodes
        Space: O(h) where h is tree height
        """
        if not root:
            return []
        
        result = []
        stack = []
        current = root
        last_visited = None

        while current or stack:
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left
            
            # Peek at the top node
            peek = stack[-1]

            # If right child exists and hasn't been visited yet
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                # Process current node
                result.append(peek.val)
                last_visited = stack.pop()
        
        return result