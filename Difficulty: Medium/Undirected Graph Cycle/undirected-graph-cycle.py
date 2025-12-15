from collections import deque, defaultdict

class Solution:
	def isCycle(self, V, edges):
	    """
	    Detect cycle in an undirected graph using BFS
	    
	    Args:
	        V: Number of vertices
	        edges: List of edges [u, v]
	    
	    Returns:
	        True if cycle exists, False otherwise
	    """
	    # Build adjacency list
		adj = defaultdict(list)
		for u, v in edges:
		    adj[u].append(v)
		    adj[v].append(u)
		
		visited = [False] * V
		
		# Check each component
		for node in range(V):
		    if not visited[node]:
		        if self.bfs_detect_cycle(node, adj, visited):
		            return True
		
		return False
	
	def bfs_detect_cycle(self, start: int, adj: dict, visited: list[bool]) -> bool:
	    """
	    BFS traversal to detect cycle in a component
	    
	    Args:
	        start: Starting node
	        adj: Adjacency list
	        visited: Visited array
	       
	    Returns:
	        True if cycle found in this component
	    """
	    queue = deque([(start, -1)]) # (node, parent)
		visited[start] = True
		
		while queue:
		    node, parent = queue.popleft()
		    
		    # Check all neighbors
		    for neighbor in adj[node]:
		        if not visited[neighbor]:
		            visited[neighbor] = True
		            queue.append((neighbor, node))
		        # If neighbor is visited and not parent, cycle found
		        elif neighbor != parent:
		            return True
		
		return False