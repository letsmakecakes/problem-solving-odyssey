class Solution:
    def dfs(self, adj):
        """
        Perform depth-first search traversal on a graph starting from node 0.
        
        Args:
            adj: Adjacency list representation of the graph
        
        Returns:
            List of nodes in DFS traversal order
        """
        visited = set([0])
        traversal = []
        
        def explore(node):
            traversal.append(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    explore(neighbor)
        
        explore(0)
        
        return traversal