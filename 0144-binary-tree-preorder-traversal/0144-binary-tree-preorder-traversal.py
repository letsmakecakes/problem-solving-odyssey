# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs preorder traversal of a binary tree.
        Time: O(n), Space: O(h) where h is the height
        """
        if not root:
            return []
        
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push the right first so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result