# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: empty tree or found the value
        if not root or root.val == val:
            return root
        
        # Search in the appropriate subtree based on BST property
        return self.searchBST(root.right, val) if val > root.val else self.searchBST(root.left, val)