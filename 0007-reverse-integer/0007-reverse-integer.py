class Solution:
    """A class to handle integer reversal with 32-bit integer overflow checking."""

    # Class constants for 32-bit integer bounds
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31

    def reverse(self, x: int) -> int:
        """
        Reverse the digits of an integer while handling 32-bit integer overflow.

        Args:
            x (int): The integer to reverse
        
        Returns:
            int: The reverse integer, or 0 if the result would overflow
        """
        # Handle the sign separately using the sign function
        sign = -1 if x < 0 else 1

        # Convert to string, reverse it, and back to integer
        # Using string manipulation is more readable and often faster
        # for this specific use case
        try:
            result = sign * int(str(abs(x))[::-1])

            # Check for 32-bit integer overflow
            if self.MIN_INT <= result <= self.MAX_INT:
                return result
            
            return 0
        except ValueError:
            return 0