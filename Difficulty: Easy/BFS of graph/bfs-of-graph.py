from collections import deque

class Solution:
    def bfs(self, adj):
        """
        Perform breadth-first search traversal on a graph starting from node 0.
        
        Args:
            adj: Adjacency list representation of the graph
        
        Returns:
            List of nodes in BFS traversal order
        """
        if not adj:
            return []
        
        visited = set([0])
        traversal = []
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            traversal.append(node)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            
        
        return traversal