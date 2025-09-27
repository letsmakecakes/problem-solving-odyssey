class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determine if a sequence of moves returns to the origin.

        Args:
            moves: String containing 'U', 'D', 'L', 'R' characters

        Returns:
            bool: True if the moves return to origin (0, 0)
        """
        # Early return for empty string (already at origin)
        if not moves:
            return True
        
        # Count moves in each direction
        move_counts = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for move in moves:
            move_counts[move] += 1
        
        # Check if opposite moves cancel out
        return (move_counts['U'] == move_counts['D'] and move_counts['L'] == move_counts['R'])
