class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        Counts the total number of digit '1' appearing in all numbers from 0 to n.
        Uses pattern recognition to acheive O(log n) time complexity.

        Args:
            n (int): Upper bound number (inclusive). Must be non-negative.
        
        Returns:
            int: Total count of digit '1' in range [0, n].
        
        Raises:
            ValueError: If n is negative.
        """
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")
        if n < 0:
            raise ValueError("Input be non-negative")
        if n == 0:
            return 0
        
        count = 0
        place_value = 1

        while place_value <= n:
            # Calculate divisor and remainder for current place value
            divisor = place_value * 10
            quotient = n // divisor
            remainder = n % divisor
            current_digit = (n // place_value) % 10

            # Count 1's at current place value using pattern recognition
            if current_digit > 1:
                count += (quotient + 1) * place_value
            elif current_digit == 1:
                count += quotient * place_value + (remainder - place_value + 1)
            else: # current_digit == 0
                count += quotient * place_value
            
            place_value *= 10
        
        return count
        
        return count