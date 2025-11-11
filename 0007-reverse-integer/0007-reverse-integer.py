class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse the digits of a 32-bit signed integer.
        Returns 0 if the reversed integer overflows.
        """
        # Extract sign and work with absolute value
        sign = -1 if x < 0 else 1
        reversed_num = int(str(abs(x))[::-1]) * sign
        
        # Check 32-bit signed integer bounds
        return reversed_num if -2**31 <= reversed_num <= 2**31 - 1 else 0