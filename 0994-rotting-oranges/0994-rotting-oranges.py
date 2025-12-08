from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh_oranges = 0

        # Find all initially rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        # If no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
        
        # BFS to spread the rot
        minutes = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            # Process all oranges that rot in this minute
            size = len(queue)

            for _ in range(size):
                x, y = queue.popleft()

                # Check all 4 adjacent cells
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    # If adjacent cell has a fresh orange
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 # Make it rotten
                        fresh_oranges -= 1
                        queue.append((nx, ny))       
            
            # Increment minutes after processing this level
            if queue:   # Only increment if there are more oranges to process
                minutes += 1
        
        # If there are still fresh oranges, return -1
        return minutes if fresh_oranges == 0 else -1
