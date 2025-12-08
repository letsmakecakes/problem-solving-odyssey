class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Perform flood fill on an image starting from position (sr, sc)
        
        Time Complexity: O(m * n) where m = rows, n = cols
        Space Complexity: O(m * n) for recursion stack in worst case
        """
        # Get the original color
        original_color = image[sr][sc]
        
        # If the original color is the same as new color, no work needed
        if original_color == color:
            return image
        
        # Get dimensions
        rows, cols = len(image), len(image[0])
        
        def dfs(r, c):
            # Base cases: out of bounds or different color
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original_color:
                return
            
            # Change the color
            image[r][c] = color
            
            # Recursively fill in all 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Start the flood fill
        dfs(sr, sc)
        return image
            