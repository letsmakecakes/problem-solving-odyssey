# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative inorder traversal using a stack.
        Time: O(n), Space: O(h) where h is tree height
        """
        result = []
        stack = []
        node = root

        while node or stack:
            # Traverse to leftmost node, pushing all nodes onto stack
            while node:
                stack.append(node)
                node = node.left
            
            # Process node (visit after left subtree)
            node = stack.pop()
            result.append(node.val)

            # Explore right subtree
            node = node.right
        
        return result