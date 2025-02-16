class Solution:
    """A class to check if a number is a palindrome."""

    def isPalindrome(self, x: int) -> bool:
        """
        Determine if an integer is a palindrome.
        A number is a palindrom when it reads the same backward as forward.

        Args:
            x(int): The number to check
        
        Returns:
            bool: True if the number is a palindrome, False otherwise
        """
        # Negative numbers are not palindromes
        # Numbers ending with 0 are only palindromes if the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        # Only need to reverse half the number
        # When reversed_half becomes >= original number,
        # we've reached the middle
        while x > reversed_half:
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
        
        # If length is odd, we need to remove middle digit
        # Example: 12321 -> x = 12, reversed_half = 123
        # After removing middle: x = 12, reversed_half = 12
        return x == reversed_half or x == reversed_half // 10