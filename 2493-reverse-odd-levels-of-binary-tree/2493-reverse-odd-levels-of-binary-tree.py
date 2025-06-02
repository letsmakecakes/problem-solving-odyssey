# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque([root])
        level = 0

        while queue:
            level_nodes = self._get_current_level_nodes(queue)

            # Reverse values if current level is odd
            if level % 2 == 1:
                self._reverse_level_values(level_nodes)
            
            # Add children of current level to queue
            self._add_children_to_queue(level_nodes, queue)
            level += 1
        
        return root

    
    def _get_current_level_nodes(self, queue: deque) -> list[TreeNode]:
        """Extract all nodes from the current level."""
        level_nodes = []
        level_size = len(queue)
            
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node)
        
        return level_nodes
    
    def _reverse_level_values(self, nodes: list[TreeNode]) -> None:
        """Reverse the values of nodes in the current level."""
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
            left += 1
            right -= 1
            
    
    def _add_children_to_queue(self, nodes: list[TreeNode], queue: deque) -> None:
        """Add children of current level nodes to the queue."""
        for node in nodes:
            if node.left:
                queue.append(node.left)
                queue.append(node.right)
            
