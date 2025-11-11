class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check if an integer is a palindrome.
        Negative numbers are not palindromes.
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10 (ignore middle digit)
        return x == reversed_half or x == reversed_half // 10
