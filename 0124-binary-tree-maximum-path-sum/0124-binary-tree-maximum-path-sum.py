# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def max_gain(node):
            nonlocal max_sum

            if not node:
                return 0
            
            # Only consider positive contributions from children
            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            # Update global maximum with path through current node
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Return maximum gain if we continue the path through this node
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return max_sum