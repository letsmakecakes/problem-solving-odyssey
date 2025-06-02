# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Handle edge case: add at root level
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        # Handle null root after depth check
        if not root:
            return root
        
        # BFS to find nodes at target depth - 1
        queue = deque([root])
        current_depth = 1

        # Traverse to the level just before target depth
        while queue and current_depth < depth - 1:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1
        
        # Add new row by inserting new nodes
        while queue:
            node = queue.popleft()
            self._insert_new_nodes(node, val)
        
        return root
    
    def _insert_new_nodes(self, parent: TreeNode, val: int) -> None:
        """Insert new nodes with given value between parent and its children."""\
        # Create new left node and connect it
        new_left = TreeNode(val)
        new_left.left = parent.left
        parent.left = new_left

        # Create new right node and connect it
        new_right = TreeNode(val)
        new_right.right = parent.right
        parent.right = new_right
