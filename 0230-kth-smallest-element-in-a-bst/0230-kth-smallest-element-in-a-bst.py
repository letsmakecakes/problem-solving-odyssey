# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        def traverse(current_node):
            if current_node is None:
                return
            traverse(current_node.left)
            nodes.append(current_node.val)
            traverse(current_node.right)
        
        traverse(root)
            
        if k > len(nodes):
            return None
        
        return nodes[k-1]