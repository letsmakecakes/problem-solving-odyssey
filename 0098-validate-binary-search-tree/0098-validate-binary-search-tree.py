# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        results = []
        
        def traverse(current_node):
            if current_node is None:
                return
            traverse(current_node.left)
            results.append(current_node.val)
            traverse(current_node.right)
        
        traverse(root)
        
        for i in range(1, len(results)):
            if results[i] <= results[i-1]:
                return False
        
        return True