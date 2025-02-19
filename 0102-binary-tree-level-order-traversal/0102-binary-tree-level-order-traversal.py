# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level-order traversal of a binary tree.

        Args:
            root: Root node of the binary tree.
        
        Returns:
            List of lists containing values at each level of the tree.
        """
        if not root:
            return []
        
        return self._process_tree_levels(root)
    
    def _process_tree_levels(self, root: TreeNode) -> List[List[int]]:
        """
        Helper method to process tree levels using BFS.

        Args:
            root: Non-null root node of the binary tree.
        
        Returns:
            List of lists containing values at each level.
        """
        result = []
        queue = deque([root])

        while queue:
            level_values = self._process_current_level(queue)
            result.append(level_values)
        
        return result
    
    def _process_current_level(self, queue: deque) -> List[int]:
        """
        Processes nodes at the current level and enqueues their children.

        Args:
            queue: Queue containing nodes to process at current level.
        
        Returns:
            List of values from nodes at current level.
        """
        level_size = len(queue)
        level_values = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_values.append(node.val)

            self._enqueue_children(queue, node)
        
        return level_values
    
    def _enqueue_children(self, queue: deque, node: TreeNode) -> None:
        """
        Enqueues the left and right children of a node if they exist.

        Args:
            queue: Queue to add children to.
            node: Node whose children should be enqueued.
        """
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)