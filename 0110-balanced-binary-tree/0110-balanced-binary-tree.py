# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if a binary tree is height-balanced.
        A tree is balanced if the height difference between left and right subtrees is at most 1 for every node
        """
        def get_height(node: Optional[TreeNode]) -> int:
            """
            Returns the heiht of the subtree, or -1 if unbalanced.

            Args:
                node: Root of the current subtree
            
            Returns:
                Height of subtree if balanced, -1 otherwise
            """
            if not node:
                return 0
            
            # Check left subtree
            left_height = get_height(node.left)
            if left_height == -1:
                return -1
            
            # Check right subtree
            right_height = get_height(node.right)
            if right_height == -1:
                return -1
            
            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)
        
        return get_height(root) != -1
