# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # List to store the right side view
        right_side_view = []

        def traverse(current, level):
            if not current:
                return
            
            # If this the first time we are visiting this level, add the node's value
            if level == len(right_side_view):
                right_side_view.append(current.val)
            
            # Traverse the right subtree first, then the left subtree
            traverse(current.right, level + 1)
            traverse(current.left, level + 1)
        
        traverse(root, 0)
        return right_side_view