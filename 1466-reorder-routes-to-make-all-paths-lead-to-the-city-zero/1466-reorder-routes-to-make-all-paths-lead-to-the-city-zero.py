from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Find minimum number of edge reversals to make all paths lead to city 0.
        
        Approach: DFS/BFS from city 0, count edges pointing away from 0
        Time: O(n), Space: O(n)
        """
        graph = defaultdict(list)
        
        for a, b in connections:
            graph[a].append((b, 1))  # Original direction
            graph[b].append((a, 0))  # Reverse direction
        
        visited = set()
        
        def dfs(city):
            visited.add(city)
            count = 0
            
            for neighbor, needs_reversal in graph[city]:
                if neighbor not in visited:
                    count += needs_reversal + dfs(neighbor)
            
            return count
        
        return dfs(0)