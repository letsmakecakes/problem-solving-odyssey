class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the longest palindrom substring for this center
            return s[left + 1:right]
        
        longest = ""
        for i in range(len(s)):
            # Check for odd-length palindromes
            odd_palindrome = expandAroundCenter(i, i)
            # Check for even-length palindromes
            even_palindrome = expandAroundCenter(i, i + 1)
            # Update the longest palindrome found
            longest = max(longest, odd_palindrome, even_palindrome, key=len)

        return longest