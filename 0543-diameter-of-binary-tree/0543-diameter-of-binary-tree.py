# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            """Returns height and updates max_diameter as side effect."""
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Update global maximum
            dfs.max_diameter = max(dfs.max_diameter, left + right)

            return 1 + max(left, right)
        
        # Initialize function attribute
        dfs.max_diameter = 0
        dfs(root)
        return dfs.max_diameter